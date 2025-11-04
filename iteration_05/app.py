from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    contact_info = {
        "email": "jbracke26@nmhschool.org",
        "github": "github.com/jbracke26",
        "phone": None 
    }
    return render_template("contact.html", contact_info=contact_info)

@app.route("/about")
def about():
    return render_template("about.html", author="Henry Bracke")

app.run(debug=True)