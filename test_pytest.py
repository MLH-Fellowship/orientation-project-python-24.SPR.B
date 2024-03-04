"""
Tests in Pytest
"""

from app import app


def test_client():
    """
    Makes a request and checks the message received is the same
    """
    response = app.test_client().get("/test")
    assert response.status_code == 200
    assert response.json["message"] == "Hello, World!"


def test_post_person():
    """
    Tests adding a person
    """
    person = {
        "phone_number": "+2348100000000",
        "email": "firstt@test.com",
        "name": "Dave",
    }

    existing_person = (
        app.test_client()
        .get("/resume/person", headers={"content-type": "application/json"})
        .json["data"]
    )
    if existing_person is None:
        app.test_client().post(
            "/resume/person", json=person, headers={"content-type": "application/json"}
        )

        new_person = (
            app.test_client()
            .get("/resume/person", headers={"content-type": "application/json"})
            .json["data"]
        )

        assert new_person["name"] == person["name"]
        assert new_person["name"] == person["name"]
        assert new_person["phone_number"] == person["phone_number"]


def test_put_person():
    """
    Tests updating a person if person exists, otherwise create person if person does not exists
    """
    person = {
        "phone_number": "+2348100000001",
        "email": "second@test.com",
        "name": "John",
    }

    app.test_client().put("/resume/person", json=person)

    new_person = (
        app.test_client()
        .get("/resume/person", headers={"content-type": "application/json"})
        .json["data"]
    )

    assert new_person["name"] == person["name"]
    assert new_person["name"] == person["name"]
    assert new_person["phone_number"] == person["phone_number"]


def test_experience():
    """
    Add a new experience and then get all experiences.

    Check that it returns the new experience in that list
    """
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png",
    }

    item_id = (
        app.test_client().post("/resume/experience", json=example_experience).json["id"]
    )
    response = app.test_client().get("/resume/experience")
    assert response.json[item_id] == example_experience


def test_education():
    """
    Add a new education and then get all educations.

    Check that it returns the new education in that list
    """
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png",
    }
    item_id = (
        app.test_client().post("/resume/education", json=example_education).json["id"]
    )

    response = app.test_client().get("/resume/education")
    assert response.json[item_id] == example_education


def test_skill():
    """
    Add a new skill and then get all skills.

    Check that it returns the new skill in that list
    """
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png",
    }

    item_id = app.test_client().post("/resume/skill", json=example_skill).json["id"]

    response = app.test_client().get("/resume/skill")
    assert response.json[item_id] == example_skill
