from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Eu sunt homepage</p>"

_users = ["george", "john", "mary", "anne", "ginger"]

@app.route("/users/")
def users():
    return """
        <ul>
            %s
        </ul>
        """ % "\n".join(
            f"<li>{user}</li>"
            for user in _users
        )

@app.route("/users/<id>")
def user(id):
    return f"<p>Salut {id}!!</p>"