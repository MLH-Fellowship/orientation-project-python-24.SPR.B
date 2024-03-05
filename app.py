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
        # Return existing experience data
        return jsonify(data["experience"])

    if request.method == 'POST':
        # Parse JSON data from request body
        new_experience_data = request.json
        # Create a new Experience object
        new_experience = Experience(new_experience_data["title"],
                                    new_experience_data["company"],
                                    new_experience_data["start_date"],
                                    new_experience_data["end_date"],
                                    new_experience_data["description"],
                                    new_experience_data["logo"])
        # Add the new experience to the data dictionary
        data["experience"].append(new_experience)
        return jsonify({"message": "Experience added successfully"})

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
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/experience/reorder', methods=['POST'])
def reorder_experience():
    '''
    Handle reordering of experience section
    '''
    req_data = request.get_json()
    if req_data and 'order' in req_data:
        new_order = req_data['order']
        if len(new_order) == len(data['experience']):
            data['experience'] = [data['experience'][idx] for idx in new_order]
            return jsonify({"message": "Experience reordered successfully"})

    return jsonify({"message": "Invalid data provided"}), 400

@app.route('/resume/education/reorder', methods=['POST'])
def reorder_education():
    '''
    Handle reordering of education section
    '''
    req_data = request.get_json()
    if req_data and 'order' in req_data:
        new_order = req_data['order']
        if len(new_order) == len(data['education']):
            data['education'] = [data['education'][idx] for idx in new_order]
            return jsonify({"message": "Education reordered successfully"})

    return jsonify({"message": "Invalid data provided"}), 400

@app.route('/resume/skill/reorder', methods=['POST'])
def reorder_skill():
    '''
    Handle reordering of skill section
    '''
    req_data = request.get_json()
    if req_data and 'order' in req_data:
        new_order = req_data['order']
        if len(new_order) == len(data['skill']):
            data['skill'] = [data['skill'][idx] for idx in new_order]
            return jsonify({"message": "Skill reordered successfully"})

    return jsonify({"message": "Invalid data provided"}), 400
