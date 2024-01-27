'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        index = request.args.get('index')
        if index is not None:
            try:
                index = int(index)
                specific_skill = data["skill"][index]
                return jsonify({"name": specific_skill.name, "proficiency": specific_skill.proficiency, "logo": specific_skill.logo})
            except (IndexError, ValueError):
                return jsonify({"error": "Invalid index provided"}), 400
        else:
            return jsonify([{"name": skill.name, "proficiency": skill.proficiency, "logo": skill.logo} for i, skill in enumerate(data["skill"])])

    if request.method == 'POST':
        new_skill = {
            "name": request.json.get("name"),
            "proficiency": request.json.get("proficiency"),
            "logo": request.json.get("logo")
        }

        skill_index = len(data["skill"])
        data["skill"].append(Skill(**new_skill))
        return jsonify({"id": skill_index})

    return jsonify({})
