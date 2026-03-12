from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret_key"

# Fixed credentials
accounts = [
    {"email": "mer@gmail.com", "password": "mast123", "role": "mater"},
    {"email": "hastpatel77@gmail.com", "password": "sissyhast", "role": "slave"},
    {"email": "slave2@gmail.com", "password": "slave234", "role": "slave"}
]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = next((u for u in accounts if u["email"] == email and u["password"] == password), None)
        if user:
            session["user"] = email
            session["role"] = user["role"]
            if user["role"] == "master":
                return redirect("/dashboard_master")
            else:
                return redirect("/dashboard_slave")
        return "Invalid credentials"
    return render_template("login.html")
