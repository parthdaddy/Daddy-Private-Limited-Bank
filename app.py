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
# Fixed Deposit Page (Slave)
@app.route("/fd")
def fd():
    if session.get("role") != "slave":
        return "Access Denied"
    user = next((u for u in accounts if u["email"] == session["user"]), None)
    return render_template("fd.html", user=user)

# Share Market Page (Slave)
@app.route("/shares")
def shares():
    if session.get("role") != "slave":
        return "Access Denied"
    user = next((u for u in accounts if u["email"] == session["user"]), None)
    share_price = 500  # Example fixed share price
    return render_template("shares.html", user=user, share_price=share_price)
