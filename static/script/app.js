let placeName = document.getElementById("placeName");
let submit = document.getElementById("submit");
let confirm = document.getElementById("confirm");
let Cbtn = document.getElementById("Cbtn");
let Rbtn = document.getElementById("Rbtn");
let placeForm = document.getElementById("placeForm");
let memBer  = document.getElementById("member");


let currentSlide=0;
const slides=document.querySelectorAll('.slide');
slides[currentSlide].classList.add('active');


function changeSlide(direction){
    slides[currentSlide].classList.remove('active');
    currentSlide=(currentSlide+direction+slides.length)%slides.length;

    slides[currentSlide].classList.add('active');
}
//Automatic slide  change 
setInterval(()=>{
    changeSlide(1);
},3000);
 

submit.addEventListener("click",function(event){
    let dateInput = document.getElementById("date").value;
    let currentDate = new Date();
    let selectedDate = new Date(dateInput);
    let datalist = document.getElementById("places");
    options = Array.from(datalist.options).map(opt => opt.value.toLowerCase());
    let enteredValue = placeName.value.trim().toLowerCase();
    today,setHours(0,0,0,0);

  
    if(!options.includes(enteredValue)){
        alert("Please select a name from the options provided.")
        event.preventDefault();
    }
    else if(placeName.value == "" || date.value == ""){
        alert("Please Fill Form!")
        event.preventDefault();
    }
    else if(selectedDate < currentDate){
        alert("Please Select A Future Date")
        event.preventDefault();
    }
    else if(memBer.value <= 0 ){
        alert("please enter a valid member number")
        event.preventDefault();
    }
    else{
        alert("Taxi for " + placeName.value + " is proceeding make payment for booking")
    }
})

confirm.addEventListener("click",function(event){
    let your_name = document.getElementById("your_name").value;
    let your_email = document.getElementById("your_email").value;
    let dateInput1 = document.getElementById("checkin").value;
    let dateInput2 = document.getElementById("checkout").value;
    let currentDate = new Date();
    let selectedDate1 = new Date(dateInput1);
    let selectedDate2 = new Date(dateInput2);
    let usernamecheck = /^[A-Za-z. ]{5,30}$/;
    let emailnamecheck = /^[A-Za-z_]{3,}[0-9]{2,}@[A-Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;

    if(your_name == "" || your_email == "" || dateInput1 == "" || dateInput2 == ""){
            alert("Please Fill Form!")
            event.preventDefault();
        }
    else if(selectedDate1 < currentDate){
        alert("Please Select A Future Date")
        event.preventDefault();
    }
    else if(selectedDate2 < currentDate){
        alert("Please Select A Future Date")
        event.preventDefault();
    }
    else if(!usernamecheck.test(your_name)){
        alert("Please Fill Correct Name")
        event.preventDefault();
    }
    else if(!emailnamecheck.test(your_email)){
        alert("Please Fill Correct Email")
        event.preventDefault();
    }
    else if(document.querySelector('script[alert-error]')){
        return;
    }
    else{
        alert("Your Room is Booked")
    }
})


Cbtn.addEventListener("click", function(event){
    let N = document.getElementById("N").value;
    let E = document.getElementById("E").value;
    let emailcheck = /^[A-Za-z_]{3,}[0-9]{2,}@[A-Za-z]{3,}[.]{1}[A-Za-z.]{2,6}$/;
    let usercheck = /^[A-Za-z. ]{5,30}$/;
     
    if(N.trim() === "" || E.trim() === ""){
        alert("Please Fill Details")
        event.preventDefault();
    }
    else if(!usercheck.test(N)){
        alert("Please Fill Correct Name")
        event.preventDefault();
    }
    else if(!emailcheck.test(E)){
        alert("Please Fill Correct Email")
        event.preventDefault();
    }
    else if(document.querySelector('script[alert-error]')){
        event.preventDefault();
        return;
    }
    else{
        alert("You Connect With Us")
    }
})











