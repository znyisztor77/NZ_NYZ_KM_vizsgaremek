


function login() {
    var username = document.getElementById("username").value;
    var psw = document.getElementById("password").value;
   
    if(username == "Admin" && psw == "1234"){
        alert("Sikeres bejelentkezés Admin!")
        
        window.open('admin.html');
        
        
    }else if(username == "Raktár" && psw == "1234"){
        alert("Sikeres bejelentkezés Raktár!")
        
        window.open('raktar.html');
        

    }else if(username == "Béla" && psw == "1234"){
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