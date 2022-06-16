from flask import Flask, render_template, request, flash
from models import get_posts, create_post
from flask_cors import CORS
from datetime import datetime
from better_profanity import profanity

app = Flask(__name__)

app.config["SECRET_KEY"] = "this is my sexret key"

CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        pass

    if request.method == "POST":
        profanity.load_censor_words()
        name = profanity.censor(request.form.get("name"))
        post = profanity.censor(request.form.get("post"))
        if name != "" and post != "":
            current_id = int(open("id.txt", "r").read())
            creation_date = datetime.now().strftime("%m/%d/%y %H:%M:%S")
            create_post(current_id, name, post, creation_date)
            flash("New post created")
            current_id += 1
            with open("id.txt", "w") as fl:
                fl.write(str(current_id + 1))
                fl.close()
        else:
            flash("Missing name or content for post")

    posts = get_posts()

    return render_template("index.html", posts=reversed(posts))