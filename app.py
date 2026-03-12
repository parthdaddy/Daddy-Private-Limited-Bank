from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/bank")
db = client.bank

# Login route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = db.users.find_one({"email": email, "password": password})
        if user:
            session["user"] = email
            session["role"] = user["role"]
            if user["role"] == "master":
                return redirect("/dashboard_master")
            else:
                return redirect("/dashboard_slave")
        return "Invalid credentials"
    return render_template("login.html")

# Master Dashboard
@app.route("/dashboard_master", methods=["GET", "POST"])
def dashboard_master():
    if session.get("role") != "master":
        return "Access Denied"
    users = list(db.users.find({"role":"slave"}))
    fd = db.fd.find_one()
    shares = db.shares.find_one()
    return render_template("dashboard_master.html", users=users, fd=fd, shares=shares)

# Slave Dashboard
@app.route("/dashboard_slave")
def dashboard_slave():
    if session.get("role") != "slave":
        return "Access Denied"
    user = db.users.find_one({"email": session["user"]})
    shares = db.shares.find_one()
    return render_template("dashboard_slave.html", user=user, shares=shares)

# Run server
if __name__ == "__main__":
    app.run(debug=True)
