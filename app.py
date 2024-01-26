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

@app.route('/')
def index():
    return jsonify({'message':'Hi User'})

@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST','PUT'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        return jsonify({})
    
    if request.method == 'PUT':
        experience = data['experience'][0]
          
        if 'title' in request.json:
            experience.title = request.json['title']
        if 'description' in request.json:
            experience.description = request.json['description']
        if 'company' in request.json:
            experience.company = request.json['company']
        if 'start_date' in request.json:
            experience.start_date = request.json['start_date']
        if 'end_date' in request.json:
            experience.end_date = request.json['end_date']
        if 'logo' in request.json:
            experience.logo = request.json['logo']
        
        
        return jsonify({'message':'experience updated','updated_experience':experience.__dict__})

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
