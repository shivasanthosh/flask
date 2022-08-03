from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify
app = Flask(__name__)


# @app.route("/shiva")
# def shiva():
#     return "Hello shiva!"

# @app.route("/<name>")
# def hello_name(name):
#     return "Hello {}!".format(name)

# @app.route("/<name>/<int:age>")
# def hello_name_age(name, age):
#     return "Hello {}! You are {} years old!".format(name, age)

"""1. Add a View Function for the Home page."""
@app.route("/")
def home():
    return render_template("home.html")

"""2. Add a View Function for the About page."""
@app.route("/about")
def about():
    return render_template("about.html")


    

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)