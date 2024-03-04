# pylint: disable=R0913

"""
Models for the Resume API. Each class is related to
"""
from re import match
from dataclasses import dataclass


@dataclass
class Experience:
    """
    Experience Class
    """

    title: str
    company: str
    start_date: str
    end_date: str
    description: str
    logo: str


@dataclass
class Education:
    """
    Education Class
    """

    course: str
    school: str
    start_date: str
    end_date: str
    grade: str
    logo: str


@dataclass
class Skill:
    """
    Skill Class
    """

    name: str
    proficiency: str
    logo: str


@dataclass
class Person:
    """
    Person Class
    """

    name: str
    phone_number: str
    email: str

    def is_number_in_international_format(self):
        """Checks if the phone number adheres to international standard"""
        pattern = "^\\+?[1-9][0-9]{7,14}$"
        return match(pattern, self.phone_number) is not None

    def is_email_valid(self):
        """Returns True if the email provided is valid, otherwise False"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return match(pattern, self.email) is not None
