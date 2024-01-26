# pylint: disable=R0913

'''
Models for the Resume API. Each class is related to
'''

from dataclasses import dataclass


@dataclass
class Experience:
    '''
    A class representing work experience.

    Attributes:
    - title (str): The job title.
    - company (str): The name of the company.
    - start_date (str): The start date of the experience.
    - end_date (str): The end date of the experience.
    - description (str): A brief description of the experience.
    - logo (str): The path to the logo associated with the experience.
    '''

    title: str
    company: str
    start_date: str
    end_date: str
    description: str
    logo: str


@dataclass
class Education:
    '''
    A class representing educational background.

    Attributes:
    - course (str): The name of the course.
    - school (str): The name of the educational institution.
    - start_date (str): The start date of the education.
    - end_date (str): The end date of the education.
    - grade (str): The grade or GPA achieved.
    - logo (str): The path to the logo associated with the education.
    '''

    course: str
    school: str
    start_date: str
    end_date: str
    grade: str
    logo: str


@dataclass
class Skill:
    '''
    A class representing a skill.

    Attributes:
    - name (str): The name of the skill.
    - proficiency (str): The proficiency level of the skill.
    - logo (str): The path to the logo associated with the skill.
    '''

    name: str
    proficiency: str
    logo: str
