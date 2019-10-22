from flask import Flask, redirect, request, session, render_template, url_for
import gh_oauth as gh
from meta import *
from secret import *
import randstr

app = Flask(__name__)
app.secret_key = SECRET.SUPER_SECRET


# Main page
@app.route('/')
def index():
    return render_template('index.html', title='GGuide')


@app.route(META.PAGE.SUB_PAGE.LICENSE_PAGE)
def license_page():
    return render_template('LICENSE.html')


@app.route(META.PAGE.SUB_PAGE.ERROR_PAGE)
def error_page():
    return render_template('error.html')

### page ###

# GitHub OAuth
@app.route(META.PAGE.SUB_PAGE.GH_LOGIN_PAGE)
def gh_login():
    if 'gh_token' in session and session['gh_token'] is not None:
        return redirect(META.PAGE.SUB_PAGE.LOGIN_SUCCESS)

    rand_key = randstr.randstr(40)
    session['key'] = rand_key
    red = redirect('https://github.com/login/oauth/authorize?client_id={}&redirect_uri={}&state={}'
        .format
        (
        SECRET.GITHUB_CLIENT_ID,
        META.PAGE.MAIN_PAGE + META.PAGE.SUB_PAGE.GH_REDIRECT_CODE_PAGE,
        rand_key
    )
    )

    return red


@app.route(META.PAGE.SUB_PAGE.GH_LOGOUT_PAGE, methods=['GET', 'POST'])
def gh_logout():
    if request.method == 'GET':
        session['key'] = None
        session['gh_token'] = None
        return redirect('/')
    elif request.method == 'POST':
        session['key'] = None
        session['gh_token'] = None
        return 'logouted'


@app.route(META.PAGE.SUB_PAGE.GH_REDIRECT_CODE_PAGE)
def gh_oauth():
    code = str(request.args.get('code'))
    rstate = request.args.get('state')

    if (code is None) or (code == '') or (rstate is None) or (rstate == ''):
        return redirect('/error?msg=unable access')

    if session['key'] != rstate:
        return redirect('/error?msg=session mismatch')

    g = gh.GitHub_OAuth()
    g.setCode(code)
    x = g.getToken()

    session['gh_token'] = x['token']

    return redirect(META.PAGE.SUB_PAGE.LOGIN_SUCCESS)


@app.route(META.PAGE.SUB_PAGE.LOGIN_SUCCESS)
def login_success():
    return render_template('login_success.html')

### login ###

@app.route(META.PAGE.API.SESSION_CLEAR)
def session_clear():
    session.clear()
    return redirect('/')


@app.route(META.PAGE.SUB_PAGE.IS_LOGIN, methods=['GET, POST'])
def is_login():
    if not ('gh_token' in session) or session['gh_token'] is None:
        return 'no'
    else:
        return 'yes'


@app.route(META.PAGE.API.GET_POST_JSON, methods=['GET, POST'])
def get_post(group: int, post: int):
    pass

@app.route('/api/post/upload/<group>/<post>', methods=['GET, POST'])
def upload_post(group: int, post: int):
    pass

@app.route('/api/post/edit/<group>/<post>', methods=['GET, POST'])
def upload_post(group: int, post: int):
    pass

### api ###

if __name__ == '__main__':
    app.run()
