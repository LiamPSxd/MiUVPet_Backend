from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from api.di.RepositoryModule import pet
from api.di.UtilModule import message
from api.data.model.Pet import Pet
import json

class PetView(View):
    def __init__(self, repository = pet):
        self.repository = repository
        self.message = message

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0, ids = "", condition = ""):
        if request.method == "GET":
            pets = list()

            if id == 0 and ids == "" and condition == "":
                return self.getPets(pets)
            elif id > 0 and ids == "" and condition == "":
                return self.getPet(pets, str(id))
            elif id == 0 and ids != "" and condition == "":
                return self.getPetsWhereId(pets, ids)
            elif id == 0 and ids == "" and condition != "":
                condition = condition.split(",")
                return self.getPetsWhere(pets, condition[0], condition[1], condition[2])
        else:
            return self.message._lostDB_()

    def getPets(self, pets: list):
        for pet in self.repository.getPets():
            if pet is not None:
                pets.append(pet)

        return self.message.response(pets)

    def getPet(self, pets: list, idPet):
        pet = self.repository.getPet(idPet)

        if pet is not None:
            pets.append(pet)

        return self.message.response(pets)

    def getPetsWhereId(self, pets: list, ids: str):
        for id in ids.split(","):
            if id != "":
                for pet in self.repository.getPetsWhere("id", "==", int(id)):
                    if pet is not None:
                        pets.append(pet)

        return self.message.response(pets)

    def getPetsWhere(self, pets: list, key, where, value):
        if key != "" and where != "":
            for pet in self.repository.getPetsWhere(key, where, value):
                if pet is not None:
                    pets.append(pet)

        return self.message.response(pets)

    def post(self, request):
        if request.method == "POST":
            pet = Pet.from_dict(json.loads(request.body))

            if pet._id_ > -1:
                return self.message._success_() if self.repository.addPet(pet) else self.message._failed_()
            else:
                return self.message._failed_()
        else:
            return self.message._lostDB_()

    def put(self, request, id):
        if request.method == "PUT":
            if self.repository.isGetPet(str(id)):
                pet = Pet.from_dict(json.loads(request.body))

                if pet._id_ > 0:
                    return self.message._success_() if self.repository.updatePet(pet) else self.message._failed_()
                else:
                    return self.message._failed_()
            else:
                return self.message._noData_()
        else:
            return self.message._lostDB_()

    def delete(self, request, id):
        if request.method == "DELETE":
            if self.repository.isGetPet(str(id)):
                if id > 0:
                    return self.message._success_() if self.repository.deletePet(str(id)) else self.message._failed_()
                else:
                    return self.message._failed_()
            else:
                return self.message._noData_()
        else:
            return self.message._lostDB_()