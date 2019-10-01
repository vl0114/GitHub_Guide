from flask import Flask, redirect, request, session, render_template
import gh_oauth as gh
from meta import *
from secret import *

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


# Main page
@app.route('/')
def hello_world():
    return 'Hello World!'


# GitHub OAuth
@app.route(META.PAGE.SUB_PAGE.GH_LOGIN_PAGE)
def gh_login():

    return render_template('login2.html')
        #redirect('https://github.com/login/oauth/authorize?client_id={}&redirect_uri={}'
         #           .format(SECRET.GITHUB_CLIENT_ID, META.PAGE.MAIN_PAGE + META.PAGE.SUB_PAGE.GH_REDIRECT_CODE_PAGE))


@app.route(META.PAGE.SUB_PAGE.GH_REDIRECT_CODE_PAGE)
def gh_oauth():
    code = str(request.args.get('code'))
    g = gh.GitHub_OAuth()
    g.setCode(code)
    x = g.getTocken()
    return str(x)


# Sign Up

'''
@app.route()
def su_signUp():
    pass

'''

if __name__ == '__main__':
    app.run()
