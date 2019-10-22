from flask import Flask, redirect, request, session, render_template
import gh_oauth as gh
from meta import *
from secret import *
import randstr


class MyFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='{_',
        block_end_string='_}',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='{#',
        comment_end_string='#}',
    ))


app = Flask(__name__)
app.secret_key = SECRET.SUPER_SECRET


# Main page
@app.route('/')
def index():
    if not('gh_token' in session) or session['gh_token'] is None:
        return render_template('index.html', title='GGuide', isLogin='false')
    else:
        return render_template('index.html', title='GGuide', isLogin='true')


# GitHub OAuth
@app.route(META.PAGE.SUB_PAGE.GH_LOGIN_PAGE)
def gh_login():
    rand_key = randstr.randstr(40)
    session['key'] = rand_key

    return redirect('https://github.com/login/oauth/authorize?client_id={}&redirect_uri={}&state={}'
        .format(
        SECRET.GITHUB_CLIENT_ID,
        META.PAGE.MAIN_PAGE + META.PAGE.SUB_PAGE.GH_REDIRECT_CODE_PAGE,
        rand_key
    )
    )


@app.route(META.PAGE.SUB_PAGE.GH_LOGOUT_PAGE)
def gh_logout():
    session['key'] = None
    session['gh_token'] = None
    return redirect('/')


@app.route(META.PAGE.SUB_PAGE.GH_REDIRECT_CODE_PAGE)
def gh_oauth():
    code = str(request.args.get('code'))

    if (code is None) or (code == '') or (code == None):
        return 'unable url'  # 허용되지않은 접근으로 리다이렉트

    g = gh.GitHub_OAuth()
    g.setCode(code)
    x = g.getToken()

    if session['key'] != request.args.get('state'):
        return 'session mismatch'  # 세션에러로 리다이렉트로 수정

    session['gh_token'] = x['token']

    return redirect('/')


@app.route(META.PAGE.SUB_PAGE.SESSION_CLEAR)
def session_clear():
    session.clear()


if __name__ == '__main__':
    app.run()
