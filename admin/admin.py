import re
from hashlib import sha256


class SignUp:

    def __init__(self, email, password, city, province):

        if re.fullmatch(
                re.compile(
                    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                ), email):
            self.email = email

        self.password = sha256(password.encode('utf-8')).hexdigest()

        if city.replace(" ", "").isalpha():
            self.city = city

        if province.replace(" ", "").isalpha():
            self.province = province


class LogIn:

    def __init__(self, email, password):
        if re.fullmatch(
                re.compile(
                    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                ), email):
            self.email = email

        self.password = sha256(password.encode('utf-8')).hexdigest()

    def __str__(self):
        return f"{self.email}, {self.password}"


class EditProfile:

    def __init__(self, email, password, city, province):

        if city.replace(" ", "").isalpha():
            self.city = city

        if province.replace(" ", "").isalpha():
            self.province = province

        if re.fullmatch(
                re.compile(
                    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                ), email):
            self.email = email

        self.password = sha256(password.encode('utf-8')).hexdigest()
