# GitHub OAuth module

# GitHub site - https://github.com/vl0114/GitHub_Guide/
# LICENSE - https://github.com/vl0114/GitHub_Guide/blob/master/LICENSE

from meta import *
from secret import *
from flask import request, session
import requests
import json


class GitHub_OAuth():
    def __init__(self):
        pass

    CLIENT_ID = SECRET.GITHUB_CLIENT_ID
    CLIENT_SECRET = SECRET.GITHUB_CLIENT_SECRET

    CLIENT_CODE = ""

    # request params
    param = {'code': '',
             'client_secret': SECRET.GITHUB_CLIENT_SECRET,
             'client_id': SECRET.GITHUB_CLIENT_ID}

    # Set self.client_code / it must call when url was redirected after user was login at github
    def setCode(self, code: str):
        self.CLIENT_CODE = code
        self.param['code'] = code

    # Request a token by self.client_code number
    def getToken(self):
        # token request
        r = requests.post(url=META.PAGE.GITHUB_TOKEN_URL, params=self.param, headers={'Accept': 'application/json'})
        ret = r.json()
        print(ret)
        token = ret['access_token']


        # user data request
        # u = requests.get(url=META.GH_API.USER, headers={'Authorization': 'token ' + token})

        return {'token': token}
