from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "secret_key"

# Fixed credentials
accounts = [
    {"email": "parth@gmail.com", "password": "vppv123", "role": "master"},
    {"email": "hastpatel77@gmail.com", "password": "sissyhast", "role": "slave"},
    {"email": "slave2@gmail.com", "password": "slave234", "role": "slave"}
]

# Login Route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = next((u for u in accounts if u["email"] == email and u["password"] == password), None)
        if user:
            session["user"] = email
            session["role"] = user["role"]
            # Debug print to confirm session
            print("Logged in user:", user)
            print("Session role:", session["role"])
            if user["role"] == "master":
                return redirect(url_for("dashboard_master"))
            else:
                return redirect(url_for("dashboard_slave"))
        return "Invalid credentials"
    return render_template("login.html")


# Master Dashboard
@app.route("/dashboard_master")
def dashboard_master():
    if session.get("role") != "master":
        return "Access Denied"
    user_email = session.get("user")
    return render_template("dashboard_master.html", user=user_email)


# Slave Dashboard
@app.route("/dashboard_slave")
def dashboard_slave():
    if session.get("role") != "slave":
        return "Access Denied"
    user_email = session.get("user")
    return render_template("dashboard_slave.html", user=user_email)


# Fixed Deposit Page (Slave)
@app.route("/fd")
def fd():
    if session.get("role") != "slave":
        return "Access Denied"
    user_email = session.get("user")
    return render_template("fd.html", user=user_email)


# Share Market Page (Slave)
@app.route("/shares")
def shares():
    if session.get("role") != "slave":
        return "Access Denied"
    user_email = session.get("user")
    share_price = 500  # Example fixed share price
    return render_template("shares.html", user=user_email, share_price=share_price)


# Logout Route
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
