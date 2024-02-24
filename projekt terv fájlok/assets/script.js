var username = document.getElementById("username");
var psw = document.getElementById("password");

function login() {
    if(username.value == "Admin" && psw.value == "1234"){
        alert("Sikeres bejelentkezés Admin!")
        
        window.open('admin.html');
        
        
    }else if(username.value == "Raktár" && psw.value == "1234"){
        alert("Sikeres bejelentkezés Raktár!")
        
        window.open('raktar.html');
        

    }else if(username.value == "Béla" && psw.value == "1234"){
        alert("Sikeres bejelentkezés Béla!")
        window.open('operator.html');
    }
    else{
        alert("Hibás adatok!  Kérem adja meg a helyes adatokat");
        document.getElementById("loginForm").reset();
    }
    
}
function closedTab() {
    window.open('login.html');
    this.close();
}