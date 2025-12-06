function validation(){
    let user_name = document.getElementById("user_name").value;
    let em = document.getElementById("em").value;
    let pass1 = document.getElementById("pass1").value;
    let pass2 = document.getElementById("pass2").value;
    let usercheck = /^[A-Za-z. ]{5,30}$/;
    let passwordcheck = /^(?=.*[0-9])(?=.*[!@#$^&*])(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
    let emailcheck = /^[A-Za-z_]{3,}[0-9]{2,}@[A-Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;

    if(usercheck.test(user_name)){
        document.getElementById('usererror').innerHTML = " ";
    }else{
        document.getElementById('usererror').innerHTML = '<span style="color: red;">** Username is Invalid</span>'; 
        return false;
    }
    if(emailcheck.test(em)){
        document.getElementById('emailerror').innerHTML = " ";
    }else{
        document.getElementById('emailerror').innerHTML = '<span style="color: red;">** Email is Invalid</span>';  
        return false;
    }
    if(passwordcheck.test(pass1)){
        document.getElementById('passworderror').innerHTML = " ";
    }else{
        document.getElementById('passworderror').innerHTML = '<span style="color: red;">** Password is Invalid</span>'; 
        return false;
    }
    if(pass1.match(pass2)){
        document.getElementById('confirmpassworderror').innerHTML = " ";
    }else{
        document.getElementById('confirmpassworderror').innerHTML = '<span style="color: red;">** Password is Not Matching</span>';  
        return false;
    }
}

function setupToggle(inputId,toggleClass){
    const input=document.getElementById(inputId);
    const toggle=document.querySelector(toggleClass);
    const icon=toggle.querySelector("i");

          toggle.addEventListener("click",function(){
            if(input.type === "password"){
                input.type = "text";
                icon.classList.replace("fa-eye","fa-eye-slash");
            }
            else{
                input.type="password";
                icon.classList.replace("fa-eye-slash","fa-eye");
            }
          });
}

setupToggle("pass1", ".toggle1");
setupToggle("pass2", ".toggle2");