function isLogin(
  func
  )
{
    const request = new XMLHttpRequest();
    request.open("GET", "/islogin");
    request.onreadystatechange = function () {
      let login = false;
      login = "yes" === request.responseText;
      func(login);
    };
    request.send();
}

function gh_login() {

  window.open("/gh_login", "github_login", "width=500, height=600");
  console.log(document.domain);
}

function gh_logout() {
  const request = new XMLHttpRequest();
  request.open("POST", "/gh_logout");
  request.onreadystatechange = function()
  {
    location.reload();
  };
  request.send();
}

function reLoad() {
  const x = function(login) {
        if(login)
        logined();
    else
        logouted();
    console.log(login);
    function logined() {
        document.getElementById('login-button').style.display = 'none';
        document.getElementById('logout-button').style.display = 'block';
    }

    function logouted() {
        document.getElementById('login-button').style.display = 'block';
        document.getElementById('logout-button').style.display = 'none';
    }
  };
  isLogin(x);
}
