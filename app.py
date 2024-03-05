'''
Flask Application
'''
from flask import Flask, jsonify, request
from autocorrect import Speller
from models import Experience, Education, Skill

app = Flask(__name__)

# Initialize the enchant dictionary
spell = Speller()

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
        jsonify({})

    if request.method == 'POST':
        jsonify({})

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

@app.route('/spellcheck', methods=['POST'])
def trigger_spellcheck():
    '''
    Spellcheck triggered by user from client. The user needs
    to provide the category and index of the entry to be spellchecked
    as query parameters. For example, /spellcheck?category=experience&index=0
    '''
    index = request.args.get('index')
    category = request.args.get('category')

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
    '''
    Uses autocorrect to perform spellcheck and update the data 
    entry with the corrected words
    '''
    if hasattr(entry, '__dict__'):  # Check if the object has a __dict__ attribute
        for attr_name, attr_value in vars(entry).items():
            if isinstance(attr_value, str):
                corrected_words = []
                for word in attr_value.split():
                    corrected_words.append(spell(word))
            setattr(entry, attr_name, ' '.join(corrected_words))
    return entry
