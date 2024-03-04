"""
Flask Application
"""

import os
from flask import Flask, jsonify, request
from autocorrect import Speller
from openai import OpenAI
from dotenv import load_dotenv
from models import Experience, Education, Skill, Person

load_dotenv()

app = Flask(__name__)

# Initialize the enchant dictionary
spell = Speller()

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
    "person":None

}


def validate_data(req_data, required_fields):
    """
    Validates the data
    """
    for field in required_fields:
        if field not in req_data:
            return False
    return True


@app.route("/test")
def hello_world():
    """
    Returns a JSON test message
    """
    return jsonify({"message": "Hello, World!"})


@app.route("/resume/experience", methods=["GET", "POST", "DELETE"])
def experience():
    """
    Handle experience requests
    """
    if request.method == "GET":
        index = request.args.get("index")
        if index is not None:
            index = int(index)
            inner_experience = data["experience"][index]
            return jsonify(
                {
                    "title": inner_experience.title,
                    "company": inner_experience.company,
                    "start_date": inner_experience.start_date,
                    "end_date": inner_experience.end_date,
                    "description": inner_experience.description,
                    "logo": inner_experience.logo,
                }
            )
        return jsonify()

    if request.method == "POST":
        jsonify({})

    if request.method == "DELETE":
        try:
            experience_id = request.get_json(force=True)["id"]

            if experience_id is not None and 0 <= experience_id < len(
                data["experience"]
            ):
                data["experience"].pop(
                    experience_id,
                )
                return (
                    jsonify({"message": "Experience deleted", "id": experience_id}),
                    200,
                )
            return jsonify({"message": "No experience found", "id": None}), 400
        except (KeyError, TypeError):
            return jsonify({"message": "No experience found", "id": None}), 400

    return jsonify({})


@app.route("/resume/person", methods=["POST", "PUT", "GET"])
def user():
    """
    Handles person requests
    Allows creation and update of person.
    Methods:
        - POST
        - PUT
        - GET
    """


    if request.method == "POST":
        person_exists = data["person"] is not None

        if person_exists:
            return jsonify({"message": "Person already exists"}), 400

        name = request.json.get("name")
        email = request.json.get("email")
        phone_number = request.json.get("phone_number")

        person = Person(name, phone_number, email)
        message= ""
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
        message = "Person added"

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
        message = "Person added"
        message = "Person added"

    if request.method == "GET":
        message = "Fetched user"
    return jsonify({"message": message, "data": data["person"]})



@app.route("/resume/education", methods=["GET", "POST"])
def education():
    """
    Handles education requests
    """
    if request.method == "GET":
        index = request.args.get("index")
        if index is not None:
            index = int(index)
            inner_education = data["education"][index]
            return jsonify(
                {
                    "course": inner_education.course,
                    "school": inner_education.school,
                    "start_date": inner_education.start_date,
                    "end_date": inner_education.end_date,
                    "grade": inner_education.grade,
                    "logo": inner_education.logo,
                }
            )
        return jsonify({})

    if request.method == "POST":
        try:
            data["education"].append(Education(**request.json))
            return jsonify({"id": len(data["education"]) - 1})
        except TypeError as valerror:
            return str(valerror), 400

    if request.method == "PUT":
        index = request.args.get("index", type=int)
        if index is not None and 0 <= index < len(data["education"]):
            update_data = request.json
            # Update the education entry at the specified index
            data["education"][index].course = update_data.get(
                "course", data["education"][index].course
            )
            data["education"][index].school = update_data.get(
                "school", data["education"][index].school
            )
            data["education"][index].start_date = update_data.get(
                "start_date", data["education"][index].start_date
            )
            data["education"][index].end_date = update_data.get(
                "end_date", data["education"][index].end_date
            )
            data["education"][index].grade = update_data.get(
                "grade", data["education"][index].grade
            )
            data["education"][index].logo = update_data.get(
                "logo", data["education"][index].logo
            )
            return jsonify(
                {"message": f"Education entry at index {index} updated successfully"}
            )

    if request.method == "DELETE":
        index = request.args.get("index", type=int)
        if index is not None and 0 <= index < len(data["education"]):
            return jsonify({"message": "Education deleted successfully"})

    return jsonify({})


@app.route("/resume/skill", methods=["GET", "POST"])
def skill():
    """
    Handles Skill requests
    """
    if request.method == "GET":
        index = request.args.get("index")
        if index is not None:
            index = int(index)
            inner_skill = data["skill"][index]
            return jsonify(
                {
                    "name": inner_skill.name,
                    "proficiency": inner_skill.proficiency,
                    "logo": inner_skill.logo,
                }
            )
        return jsonify([skill.__dict__ for skill in data["skill"]])

    if request.method == "POST":
        add_skill = {
            "name": request.json.get("name"),
            "proficiency": request.json.get("proficiency"),
            "logo": request.json.get("logo"),
        }

        data["skill"].append(Skill(**add_skill))
        return jsonify({"id": len(data["skill"]) - 1})

    return jsonify({})


@app.route("/spellcheck", methods=["POST"])
def trigger_spellcheck():
    """
    Spellcheck triggered by user from client. The user needs
    to provide the category and index of the entry to be spellchecked
    as query parameters. For example, /spellcheck?category=experience&index=0
    """
    index = request.args.get("index")
    category = request.args.get("category")

    if category not in data:
        return jsonify({"error": f"Category '{category}' not found"}), 400

    entries = data[category]

    try:
        index = int(index)
        entry = entries[index]
    except (ValueError, IndexError):
        return jsonify({"error": "Invalid index"}), 400

    corrected_entry = spell_check_and_correct(entry)

    return jsonify(corrected_entry)


def spell_check_and_correct(entry):
    """
    Uses autocorrect to perform spellcheck and update the data
    entry with the corrected words
    """
    if hasattr(entry, "__dict__"):  # Check if the object has a __dict__ attribute
        for attr_name, attr_value in vars(entry).items():
            if isinstance(attr_value, str):
                corrected_words = []
                for word in attr_value.split():
                    corrected_words.append(spell(word))
            setattr(entry, attr_name, " ".join(corrected_words))
    return entry


@app.route("/resume/experience/reorder", methods=["POST"])
def reorder_experience():
    """
    Handle reordering of experience section
    """
    req_data = request.get_json()
    if req_data and "order" in req_data:
        new_order = req_data["order"]
        if len(new_order) == len(data["experience"]):
            data["experience"] = [data["experience"][idx] for idx in new_order]
            return jsonify({"message": "Experience reordered successfully"})

    return jsonify({"message": "Invalid data provided"}), 400


@app.route("/resume/education/reorder", methods=["POST"])
def reorder_education():
    """
    Handle reordering of education section
    """
    req_data = request.get_json()
    if req_data and "order" in req_data:
        new_order = req_data["order"]
        if len(new_order) == len(data["education"]):
            data["education"] = [data["education"][idx] for idx in new_order]
            return jsonify({"message": "Education reordered successfully"})

    return jsonify({"message": "Invalid data provided"}), 400


@app.route("/resume/skill/reorder", methods=["POST"])
def reorder_skill():
    """
    Handle reordering of skill section
    """
    req_data = request.get_json()
    if req_data and "order" in req_data:
        new_order = req_data["order"]
        if len(new_order) == len(data["skill"]):
            data["skill"] = [data["skill"][idx] for idx in new_order]
            return jsonify({"message": "Skill reordered successfully"})

    return jsonify({"message": "Invalid data provided"}), 400


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


@app.route("/resume/get_chatgpt_suggestion", methods=["GET"])
def get_chatgpt_suggestion():
    """
    Get a suggestion from OpenAI's GPT-3 model using the text suggestion
    """
    text_description = request.args.get("text_description")

    if not text_description:
        return jsonify({"error": "No text description provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-instruct",
            messages=[{"role": "user", "content": text_description}],
        )
        if response.choices and response.choices[0].finish_reason == "stop":
            suggestion = response.choices[0].message["content"]
            return jsonify({"suggestion": suggestion}), 200
        return jsonify({"error": "No suggestion was generated"}), 500
    except Exception as e:
        return jsonify({"error": f"Error: {e}"}), 500
