from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret_key"

# Fixed credentials
accounts = [
    {"email": "master@gmail.com", "password": "master123", "role": "master"},
    {"email": "slave1@gmail.com", "password": "slave123", "role": "slave"},
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
