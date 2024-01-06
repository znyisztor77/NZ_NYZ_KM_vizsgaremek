


function login() {
    var username = document.getElementById("username").value;
    var psw = document.getElementById("password").value;
   
    if(username == "admin" && psw == "admin")
    {
        alert("Sikeres bejelentkezés!")
        
        window.open('admin.html');
        
        
    }
    else{
        
        alert("Hibás adatok!  Kérem adja meg a helyes adatokat");
        document.getElementById("loginForm").reset();
        
        
    }
    
}

