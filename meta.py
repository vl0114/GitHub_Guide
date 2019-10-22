# Metadata module
# Also used as a configuration file

# GitHub site - https://github.com/vl0114/GitHub_Guide/
# LICENSE - https://github.com/vl0114/GitHub_Guide/blob/master/LICENSE


class META:
    class PAGE:
        # GitHub sign up page
        GITHUB_SIGN_UP_URL = 'https://github.com/join'

        # GitHub login page
        GITHUB_LOGIN_URL = "https://github.com/login/oauth"

        # GitHub token page
        GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"

        # Main page of gg
        MAIN_PAGE = "http://localhost:5000"

        class SUB_PAGE:
            # GitHub Login Page
            GH_LOGIN_PAGE = "/gh_login"

            # GitHub Logout Page

            GH_LOGOUT_PAGE = "/gh_logout"

            # Login callback page
            GH_REDIRECT_CODE_PAGE = "/gh_cb"

            SESSION_CLEAR = "/session_clear"

    class GH_API:
        ADDRESS = 'https://api.github.com/'
        USER = ADDRESS + '/user'