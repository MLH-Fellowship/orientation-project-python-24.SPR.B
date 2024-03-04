"""
Flask Application
"""

from flask import Flask, jsonify, request
from models import Experience, Education, Skill, Person

app = Flask(__name__)

data = {
    "experience": [
        Experience(
            "Software Developer",
            "A Cool Company",
            "October 2022",
            "Present",
            "Writing Python Code",
            "example-logo.png",
        )
    ],
    "education": [
        Education(
            "Computer Science",
            "University of Tech",
            "September 2019",
            "July 2022",
            "80%",
            "example-logo.png",
        )
    ],
    "skill": [Skill("Python", "1-2 Years", "example-logo.png")],
    "person": None,  # Person("Charles", "+2348109000044", "test.email@example.com"),
}


@app.route("/test")
def hello_world():
    """
    Returns a JSON test message
    """
    return jsonify({"message": "Hello, World!"})


@app.route("/resume/experience", methods=["GET", "POST"])
def experience():
    """
    Handle experience requests
    """
    if request.method == "GET":
        return jsonify()

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/person", methods=["POST", "PUT", "GET"])
def person():
    """
    Handles person requests
    Allows creation and update of person.
    Methods:
        - POST
        - PUT
        - GET
    """
    if request.headers.get("Content-Type") != "application/json":
        return (
            jsonify(
                {
                    "message": "Unacceptable content-type",
                    "content-type": request.headers.get("Content-Type"),
                }
            ),
            400,
        )

    if request.method == "POST":
        person_exists = data["person"] is not None

        if person_exists:
            return jsonify({"message": "Person already exists"}), 400

        name = request.json.get("name")
        email = request.json.get("email")
        phone_number = request.json.get("phone_number")

        if not name or not email or not phone_number:
            return (
                {
                    "message": "required body missing",
                }
            ), 400

        person = Person(name, phone_number, email)
        if not person.is_email_valid():
            return jsonify({"message": "Invalid email"}), 400
        if not person.is_number_in_international_format():
            return (
                jsonify(
                    {"message": "Phone number must be contain country code e.g. +86"}
                ),
                400,
            )
        person = Person(name, phone_number, email)
        data["person"] = person

        return jsonify({"message": "Person added", "data": data["person"]})

    if request.method == "PUT":

        name = request.json.get("name")
        email = request.json.get("email")
        phone_number = request.json.get("phone_number")

        person = Person(name, phone_number, email)
        if not person.is_email_valid():
            return jsonify({"message": "Invalid email"}), 400
        if not person.is_number_in_international_format():
            return (
                jsonify(
                    {"message": "Phone number must be contain country code e.g. +86"}
                ),
                400,
            )
        data["person"] = person
        return jsonify({"message": "Person added", "data": data["person"]})

    if request.method == "GET":
        return jsonify({"data": data["person"], "message": "Person"})


@app.route("/resume/education", methods=["GET", "POST"])
def education():
    """
    Handles education requests
    """
    if request.method == "GET":
        index = request.values.get("id", None, type=int)
        if (
            index is not None
            and isinstance(index, int)
            and 0 <= index < len(data["education"])
        ):
            return jsonify({"id": index, "data": data["education"][index]})
        elif index is None:
            return jsonify({"data": data["education"], "id": None})

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/skill", methods=["GET", "POST"])
def skill():
    """
    Handles Skill requests
    """
    if request.method == "GET":
        return jsonify({})

    if request.method == "POST":
        return jsonify({})

    return jsonify({})
