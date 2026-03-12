function register(){

alert("Account created (Demo)");

location.href="index.html"

}

function login(){

alert("Login successful")

location.href="dashboard.html"

}

function logout(){

location.href="index.html"

}

function buyShare(name,price){

alert("You bought "+name+" share for ₹"+price)

}

function createFD(){

let amount=document.getElementById("amount").value

alert("FD created for ₹"+amount)

}

function updateBalance(){

let uid=document.getElementById("uid").value

let amount=document.getElementById("amount").value

alert("User "+uid+" balance updated to ₹"+amount)

}