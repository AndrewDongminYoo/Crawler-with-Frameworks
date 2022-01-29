from flask import Flask, render_template

from apps.v1 import app as version1

app = Flask(__name__, static_folder='assets', template_folder='templates')
app.register_blueprint(version1)


@app.route("/index")
@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
