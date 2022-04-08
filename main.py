from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import datetime

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", year=year)

if __name__ == "__main__":
    app.run()
