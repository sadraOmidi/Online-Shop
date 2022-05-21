import re
from hashlib import sha256


class SignUp:

    def __init__(self, name, mobile, city, province, email, password):

        if name.replace(" ", "").isalpha():
            self.name = name

        if city.replace(" ", "").isalpha():
            self.city = city

        if province.replace(" ", "").isalpha():
            self.province = province

        if re.compile('^(\+98|0)?9\d{9}$').search(mobile):
            self.mobile = mobile

        if re.fullmatch(
                re.compile(
                    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                ), email):
            self.email = email

        self.password = sha256(password.encode('utf-8')).hexdigest()


class LogIn:

    def __init__(self, email, password):
        if re.fullmatch(
                re.compile(
                    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                ), email):
            self.email = email

        self.password = sha256(password.encode('utf-8')).hexdigest()


class EditProfile:

    def __init__(self, name, mobile, city, province, email, password):

        if name.replace(" ", "").isalpha():
            self.name = name

        if city.replace(" ", "").isalpha():
            self.city = city

        if province.replace(" ", "").isalpha():
            self.province = province

        if re.compile('^(\+98|0)?9\d{9}$').search(mobile):
            self.mobile = mobile

        if re.fullmatch(
                re.compile(
                    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                ), email):
            self.email = email

        self.password = sha256(password.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    t = SignUp('s', '09123456789', 'e', 's', 's@s.com', 'sadra1234')
    print(type(t.password))
