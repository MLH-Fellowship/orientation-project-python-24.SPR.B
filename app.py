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
        return jsonify({"id": "Experience added successfully"})

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
