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



'''