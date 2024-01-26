'''
Tests for the Flask App using Pytest
'''

from app import app


def test_client():
    '''
    Test to ensure that the app's test client responds with a 200 status code
    and the expected message when making a GET request to /test endpoint.
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"


def test_experience():
    '''
    Test to add a new experience, retrieve all experiences, and verify that the
    new experience is present in the list.
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png"
    }

    # Add a new experience
    item_id = app.test_client().post('/resume/experience',
                                     json=example_experience).json['id']

    # Retrieve all experiences
    response = app.test_client().get('/resume/experience')

    # Check if the new experience is present in the list
    assert response.json[item_id] == example_experience


def test_education():
    '''
    Test to add a new education, retrieve all educations, and verify that the
    new education is present in the list.
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }

    # Add a new education
    item_id = app.test_client().post('/resume/education',
                                     json=example_education).json['id']

    # Retrieve all educations
    response = app.test_client().get('/resume/education')

    # Check if the new education is present in the list
    assert response.json[item_id] == example_education


def test_skill():
    '''
    Test to add a new skill, retrieve all skills, and verify that the
    new skill is present in the list.
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    # Add a new skill
    item_id = app.test_client().post('/resume/skill',
                                     json=example_skill).json['id']

    # Retrieve all skills
    response = app.test_client().get('/resume/skill')

    # Check if the new skill is present in the list
    assert response.json[item_id] == example_skill
