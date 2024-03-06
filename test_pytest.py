'''
Tests in Pytest
'''
from app import app


def test_client():
    '''
    Makes a request and checks the message received is the same
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"


def test_experience():
    '''
    Add a new experience and then get all experiences. 
    
    Check that it returns the new experience in that list
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/experience',
                                     json=example_experience).json['id']
    response = app.test_client().get('/resume/experience')
    assert response.json[item_id] == example_experience


def test_education():
    '''
    Add a new education and then get all educations. 
    
    Check that it returns the new education in that list
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }
    item_id = app.test_client().post('/resume/education',
                                     json=example_education).json['id']

    response = app.test_client().get('/resume/education')
    assert response.json[item_id] == example_education

def test_update_education():
    '''
    Test updating an existing education entry using PUT request
    '''
    # Create new data to update the existing education entry
    update_data = {
        "course": "Updated Course Name",
        "school": "Updated School Name",
        "start_date": "Updated Start Date",
        "end_date": "Updated End Date",
        "grade": "Updated Grade",
        "logo": "Updated Logo URL"
    }
    index = 0

    response = app.test_client().put(f'/resume/education?index={index}', json=update_data)

    assert response.status_code == 200
    assert response.json["message"] == f"Education entry at index {index} updated successfully"

    updated_education = app.test_client().get('/resume/education').json[index]
    assert updated_education["course"] == update_data["course"]
    assert updated_education["school"] == update_data["school"]
    assert updated_education["start_date"] == update_data["start_date"]
    assert updated_education["end_date"] == update_data["end_date"]
    assert updated_education["grade"] == update_data["grade"]
    assert updated_education["logo"] == update_data["logo"]


def test_delete_education():
    '''
    Add a new education and then delete it. 
    
    Check that it is no longer in the list
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }
    item_id = app.test_client().post('/resume/education',
                                     json=example_education).json['id']

    app.test_client().delete(f'/resume/education/{item_id}')
    response = app.test_client().get('/resume/education')
    assert item_id not in response.json

def test_skill():
    '''
    Add a new skill and then get all skills. 
    
    Check that it returns the new skill in that list
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/skill',
                                     json=example_skill).json['id']

    response = app.test_client().get('/resume/skill')
    assert response.json[item_id] == example_skill

def test_spellcheck():
    '''
    Tests the spellcheck functionality
    '''
    data_entry = {
        "title": "Softwere Develper",
        "company": "A Cool Copany",
        "start_date": "Octobr 2022",
        "end_date": "Present",
        "description": "Writing Python Codee",
        "logo": "example-logo.png"
    }

    response = app.test_client().post('/spellcheck?category=experience&index=0', json=data_entry)
    corrected_entry = response.json

    assert response.status_code == 200
    assert corrected_entry["title"] == "Software Developer"
    assert corrected_entry["company"] == "A Cool Company"
    assert corrected_entry["start_date"] == "October 2022"
    assert corrected_entry["end_date"] == "Present"
    assert corrected_entry["description"] == "Writing Python Code"
    assert corrected_entry["logo"] == "example-logo.png"
