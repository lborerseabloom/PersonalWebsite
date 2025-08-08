# Flask dependencies
from flask import (
    Flask,
    render_template,
    send_from_directory,
    jsonify,
    redirect,
    request,
    session,
    make_response,
    abort,
)

# Freeze dependencies
from flask_frozen import Freezer

# Project constants
from src import constants

# Misc. dependencies
import requests
import datetime
import time
import os

# Set our Flask config
config = {
    "TEMPLATES_AUTO_RELOAD": True,  # Auto reload Flask
}

# Define the Flask Application
app = Flask(
    __name__, static_url_path="/", static_folder="static", template_folder="templates"
)
app.config.from_mapping(config)

# Define the Freeze instance for SSR
ssr = Freezer(app)

@app.route("/")
def index():
    return render_template(
        "index.html",
        **{
            "me": constants.me,
            "social": constants.social_metadata,
            "experiences": constants.experiences,
            "education": constants.education,
            "technologies": constants.technologies,
        },
    )

@app.route("/projects")
def projects():
    return render_template(
        "projects.html",
        **{
            "me": constants.me,
            "social": constants.social_metadata,
            "experiences": constants.experiences,
            "education": constants.education,
            "technologies": constants.technologies,
            "projects": constants.projects,
        },
    )

@app.route("/r/<name>/")
def social_redirect(name):
    if name in constants.social_metadata:
        social_data = constants.social_metadata[name]
        social_data['title'] = str(name).capitalize()

        return render_template(
            "redirect.html", **{"social": constants.social_metadata[name]}
        )


@app.context_processor
def checkers():
    def main_metadata(value):
        return constants.main_metadata[value]

    def social_metadata(name, value):
        return constants.social_metadata[name][value]

    return dict(main_metadata=main_metadata, social_metadata=social_metadata)

# Only register dynamic routes if not using SSR
if not constants.ssr:
    from src.spotify import spotify
    app.register_blueprint(spotify)
