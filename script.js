async function login(){

let userid = document.getElementById("userid").value
let password = document.getElementById("password").value

let response = await fetch("/login",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({userid,password})
})

let data = await response.json()

if(data.success){
localStorage.setItem("token",data.token)
window.location.href="dashboard.html"
}else{
document.getElementById("message").innerText="Invalid ID or Password"
}

}
