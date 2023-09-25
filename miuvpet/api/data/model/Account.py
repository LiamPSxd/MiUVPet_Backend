from dataclasses import dataclass

@dataclass
class Account:
    def __init__(self, id = 0, name = "", email = "", password = ""):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    @property
    def _id_(self):
        return self.id

    @_id_.setter
    def _id_(self, id):
        self.id = id

    @property
    def _name_(self):
        return self.name

    @_name_.setter
    def _name_(self, name):
        self.name = name

    @property
    def _email_(self):
        return self.email

    @_email_.setter
    def _email_(self, email):
        self.email = email

    @property
    def _password_(self):
        return self.password

    @_password_.setter
    def _password_(self, password):
        self.password = password

    @staticmethod
    def from_dict(source):
        return Account(**source)

    def to_dict(self) -> dict:
        return self.__dict__

    def __repr__(self):
        return f"Account(\
                id = {self._id_}, \
                name = {self._name_}, \
                email = {self._email_}, \
                password = {self._password_}\
            )"