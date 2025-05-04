from flask import Flask
from flask import render_template

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
    app.run(debug=True)

