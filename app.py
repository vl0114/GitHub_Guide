from flask import Flask, redirect, request, session, render_template
import gh_oauth as gh
from meta import *
from secret import *
import randstr

class MyFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='{%',
    block_end_string='%}',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='{#',
    comment_end_string='#}',
  ))


app = MyFlask(__name__)
app.secret_key = SECRET.SUPER_SECRET

# Main page
@app.route('/')
def hello_world():
    return 'Hello World!'


# GitHub OAuth
@app.route(META.PAGE.SUB_PAGE.GH_LOGIN_PAGE)
def gh_login():
    rand_key = randstr.randstr(40)
    session['key'] = rand_key
    print(rand_key)
    return redirect('https://github.com/login/oauth/authorize?client_id={}&redirect_uri={}&state={}'
                    .format(
                            SECRET.GITHUB_CLIENT_ID,
                            META.PAGE.MAIN_PAGE + META.PAGE.SUB_PAGE.GH_REDIRECT_CODE_PAGE,
                            rand_key
                            )
                    )


@app.route(META.PAGE.SUB_PAGE.GH_REDIRECT_CODE_PAGE)
def gh_oauth():
    code = str(request.args.get('code'))

    if (code is None) or (code == '') or (code == None):
        return 'unable url' # 허용되지않은 접근으로 리다이렉트

    g = gh.GitHub_OAuth()
    g.setCode(code)
    x = g.getToken()

    if session['key'] != x['state']:
        return 'session mismatch' # 세션에러로 리다이렉트로 수정

    session['gh_token'] = x['token']

    return str(x) # 홉페이지 리다이렉트로 수정


# Sign Up

'''
@app.route()
def su_signUp():
    pass

'''

if __name__ == '__main__':
    app.run()
