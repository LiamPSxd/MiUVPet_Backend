from dataclasses import dataclass

@dataclass
class Pet:
    def __init__(self, id = 0, name = "", nickname = "", hunger = 0, energy = 0, health = 0, happiness = 0):
        self.id = id
        self.name = name
        self.nickname = nickname
        self.hunger = hunger
        self.energy = energy
        self.health = health
        self.hapiness = happiness

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
    def _nickname_(self):
        return self.nickname

    @_nickname_.setter
    def _nickname_(self, nickname):
        self.nickname = nickname

    @property
    def _hunger_(self):
        return self.hunger

    @_hunger_.setter
    def _hunger_(self, hunger):
        self.hunger = hunger

    @property
    def _energy_(self):
        return self.energy

    @_energy_.setter
    def _energy_(self, energy):
        self.energy = energy

    @property
    def _health_(self):
        return self.health

    @_health_.setter
    def _health_(self, health):
        self.health = health

    @property
    def _happiness_(self):
        return self.happiness

    @_happiness_.setter
    def _happiness_(self, happiness):
        self.happiness = happiness

    @staticmethod
    def from_dict(source):
        return Pet(**source)

    def to_dict(self) -> dict:
        return self.__dict__

    def __repr__(self):
        return f"Pet(\
                id = {self._id_}, \
                name = {self._name_}, \
                nickname = {self._nickname_}, \
                hunger = {self._hunger_}, \
                energy = {self._energy_}, \
                health = {self._health_}, \
                hapiness = {self._happiness_}\
            )"