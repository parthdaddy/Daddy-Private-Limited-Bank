@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]         # <-- this gets the email from login form
        password = request.form["password"]   # <-- this gets the password
        user = db.users.find_one({"email": email, "password": password})  # <-- checks in DB
        if user:
            session["user"] = email
            session["role"] = user["role"]
            if user["role"] == "master":
                return redirect("/dashboard_master")
            else:
                return redirect("/dashboard_slave")
        return "Invalid credentials"
    return render_template("login.html")
