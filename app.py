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
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST', 'PUT'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    if request.method == 'PUT':
        index = request.args.get("index", type=int)
        if index is not None and 0 <= index < len(data["education"]):
            update_data = request.json
            # Update the education entry at the specified index
            data["education"][index].course = \
            update_data.get("course", data["education"][index].course)
            data["education"][index].school = \
            update_data.get("school", data["education"][index].school)
            data["education"][index].start_date = \
            update_data.get("start_date", data["education"][index].start_date)
            data["education"][index].end_date = \
            update_data.get("end_date", data["education"][index].end_date)
            data["education"][index].grade = \
            update_data.get("grade", data["education"][index].grade)
            data["education"][index].logo = \
            update_data.get("logo", data["education"][index].logo)
            return jsonify({"message": f"Education entry at index {index} updated successfully"})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})
