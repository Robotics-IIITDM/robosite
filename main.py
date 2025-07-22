from flask import Flask, render_template
from waitress import serve
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about_us():
    return render_template("about.html")

@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/projects")
def our_projects():
    return render_template("projects.html")

@app.route("/team")
def team_data():
    return render_template("team.html")

@app.route("/contact")
def contact_us():
    return render_template("contact.html")

if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 10000))
    if os.environ.get('RENDER'):
        app.run(host='0.0.0.0', port=port)
    else:
        serve(app, host="0.0.0.0", port=port)
