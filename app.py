import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ------- CHECKING USER FUNCTION -------#
def actual_user(username):
    if "user" in session.keys():
        if session["user"] == username:
            return True

    return False

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# ------- INDEX PAGE -------#
@app.route('/')
def index():

    cocktails = list(
                mongo.db.cocktails.find({"created_by": "admin"}).limit(6))
    return render_template("index.html", cocktails=cocktails)


# ------- COCKTAILS PAGE -------#
@app.route("/")
@app.route("/get_cocktails")
def get_cocktails():
    cocktails = list(mongo.db.cocktails.find())
    return render_template("cocktails.html", cocktails=cocktails)


# ------- SEARCH COCKTAILS FUNCTION -------#
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    cocktails = list(mongo.db.cocktails.find({"$text": {"$search": query}}))
    return render_template("cocktails.html", cocktails=cocktails)


# ------- SEARCH COCKTAILS BY CATEGORY -------#
@app.route('/search_cocktails/<query>', methods=['GET', 'POST'])
def search_cocktails(query):
    if search:
        cocktails = list(
            mongo.db.cocktails.find({"category_name": query}))

    return render_template("cocktails.html", cocktails=cocktails)


# ------- REGISTER PAGE -------#
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# ------- LOGIN PAGE -------#
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back, {}!".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# ------- PROFILE PAGE -------#
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    # Display Username in session using DB data
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if not actual_user(username.lower()):
        return redirect(url_for("login"))

    if "user" in session.keys():
        if session["user"] == username:
            cocktails = list(
                mongo.db.cocktails.find({"created_by": username.lower()}))

    else:
        return redirect(url_for("login"))

    return render_template(
        "profile.html", user=user, cocktails=cocktails)


 # check for cocktails created by user / grant all access to admin
    if "user" in session.keys():
        if session["user"] == "admin":
            cocktails = list(mongo.db.cocktails.find())
        else:
            cocktails = list(
                mongo.db.cocktails.find({"created_by": username.lower()}))

        # fetch the page number from request / set the page 1
        page = int(request.args.get('page') or 1)
        num = 6

        # count documents for of pagination options
        count = ceil(float(len(cocktails) / num))

        # page - 1 checks that the first items can be found
        start = (page - 1) * num
        end = start + num
        cocktails_display = cocktails[start:end]

        return render_template(
            "profile.html", user=user, cocktails=cocktails_display,
            page=page, count=count, search=False)

    else:
        return redirect(url_for("login"))

    return render_template(
        "profile.html", user=user, cocktails=cocktails)



# ------- EDIT PROFILE -------#
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):

    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if not actual_user(username.lower()):
        return redirect(url_for("login"))

    # Update profile function
    if request.method == "POST":
        submit = {
            "username": user["username"],
            "email": user["email"],
            "password": user["password"],
        }
        mongo.db.users.update({"username": session["user"]}, submit)
        flash("Profile Updated!")

        return render_template("profile.html", user=user)

    if "user" in session:
        return render_template("edit_profile.html", user=user)

    return redirect(url_for("login"))
  

# ------- DELETE PROFILE -------#
@app.route("/delete_profile/<username>")
def delete_profile(username):


    mongo.db.users.remove({"username": username.lower()})
    flash("Profile Deleted")
    session.pop("user")

    return redirect(url_for("register"))



# ------- LOGOUT PAGE -------#
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ------- INDIVIDUAL COCKTAIL PAGE -------#
@app.route("/cocktail/<cocktail_id>")
def cocktail(cocktail_id):


    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    print(cocktail)
    return render_template("cocktail.html", cocktail=cocktail)


@app.route("/add_cocktail", methods=["GET", "POST"])
def add_cocktail():
    if request.method == "POST":
        cocktail = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_description": request.form.get("cocktail_description"),
            "cocktail_img": request.form.get("cocktail_img"),
            "image_source": request.form.get("image_source"),
            "cocktail_serv": request.form.get("cocktail_serv"),
            "cocktail_ingredients": request.form.getlist("cocktail_ingredients"),
            "cocktail_instructions": request.form.getlist("cocktail_instructions"),
            "created_by": session["user"]
        }
        mongo.db.cocktails.insert_one(cocktail)
        flash("Cocktail Added!")
        return redirect(url_for("get_cocktails"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_cocktail.html", categories=categories)


# ------- Edit Cocktail Page ------- #
@app.route("/edit_cocktail/<cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):

    
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_description": request.form.get("cocktail_description"),
            "cocktail_img": request.form.get("cocktail_img"),
            "image_source": request.form.get("image_source"),
            "cocktail_serv": request.form.get("cocktail_serv"),
            "cocktail_ingredients": request.form.getlist("cocktail_ingredients"),
            "cocktail_instructions": request.form.getlist("cocktail_instructions"),
            "created_by": session["user"]
        }
        mongo.db.cocktails.update({"_id": ObjectId(cocktail_id)}, submit)
        flash("Cocktail Updated!")
        

    cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)}) 
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_cocktail.html", cocktail=cocktail, categories=categories)


# ------- Delete Cocktail Page ------- #
@app.route("/delete_cocktail/<cocktail_id>")
def delete_cocktail(cocktail_id):
    mongo.db.cocktails.remove({"_id": ObjectId(cocktail_id)})
    flash("Cocktail Deleted")
    return redirect(url_for("get_cocktails"))


# ------- Manage Categories Page ------- #
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# ------- Add Category   ------- #
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# ------- Edit Category   ------- #
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# ------- Delete Category   ------- #
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted")
    return redirect(url_for("get_categories"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)