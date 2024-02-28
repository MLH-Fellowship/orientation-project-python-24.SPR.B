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
        index = request.args.get('index')
        if index is not None: 
            index = int(index)
            skill = data["education"][index]
            return jsonify({"course": skill.course, "school": skill.school, "start_date": skill.start_date, "end_date": skill.end_date, "grade": skill.grade, "logo": skill.logo})
        else:
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
            index = int(index)
            skill = data["skill"][index]
            return jsonify({"name": skill.name, "proficiency": skill.proficiency, "logo": skill.logo})
        else:
            return jsonify([skill.__dict__ for skill in data['skill']])

    if request.method == 'POST':
        add_skill = {
            "name": request.json.get("name"),
            "proficiency": request.json.get("proficiency"),
            "logo": request.json.get("logo")
        }

        data["skill"].append(Skill(**add_skill))
        return jsonify({"id": len(data["skill"]) - 1})

    return jsonify({})
