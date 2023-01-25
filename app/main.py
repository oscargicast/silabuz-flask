from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


@app.route("/")
def index():
    return {
        "title": "Hello",
        "description": "Desc",
    }


@app.route("/hello/")
@app.route("/hello/<name>/")
def my_controller(name: str=None):
    if not name:
        name = "world"
    name = f"Hello {name}!"
    context = {
        "name": name
    }
    return render_template("view.html", **context)


# @app.route('/suma/<num_1>/<num_2>')
# @app.route('/suma/')
# def my_sum(num_1: int=0, num_2: int=0):
#     context = {
#         'num_1': num_1,
#         'num_2': num_2,
#         'suma': num_1 + num_2,
#     }
#     return render_template("suma.html", **context)


@app.route("/suma/<int:num_1>/<int:num_2>/")
def my_sum(num_1: int = 0, num_2: int = 0):
    context = {
        'num_1': num_1,
        'num_2': num_2,
        "suma": num_1 + num_2,
    }
    return render_template("suma.html", **context)


SECRET = "secreto"

def hash_password(raw_password):
    return raw_password
    # return f"{SECRET}-{raw_password}"

def get_password(username):
    return f"{SECRET}-{username}"


@app.route("/login/", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # import ipdb; ipdb.set_trace()
        if get_password(username) == hash_password(password):
            return render_template("home.html", username=username)
        error = "No es el password"
    return render_template("login.html", error=error)


if __name__ == '__main__':
    app.run(debug=True, port=8080)