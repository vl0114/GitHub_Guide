# GitHub 유저의 정보를 관리하는 모듈

import hashlib
from psql import psql
class GH_User:

    DB = psql.psql

    def __init__(self, tokenResponse, userdataResponse):
        self.tokenResponse = tokenResponse
        self.userdataResponse = userdataResponse

    mail = '' # mail
    name = '' # GitHub Name
    gh_id = '' # GitHub ID
    gh_code = '' # GitHub 고유 코드
    follower = 0 # 팔로워 수
    repos = 0 # 리포지토리 수

    gg_token = '' # 서버용 토큰 (쿠키에 사용)

    def setToken(self):
        sha = hashlib.sha3_256()
        sha.update(self.gh_code)
        self.gg_token = sha.hexdigest()

    def saveDB(self):
        q = 'insert into gg.gguser '
        self.DB.send(q)


    def loadDB(self):
        q = 'select * from GGUSER GID = {}'.format(self.gh_id)

'''

    유저 로그인 -> 토큰으로 유저정보 조회 -> 유저 정보를 바탕으로 DB 조회
        -> 만약 DB에 정보가 없으면 DB의 정보를 저장하고 고유 토큰을 발급
    -> 고유 토큰을 시간과 조합해서 새로운 토큰 발급
    -> 쿠키로 발급

'''