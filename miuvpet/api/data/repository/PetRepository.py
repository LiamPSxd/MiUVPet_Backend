from api.data.network.DataBaseService import DataBaseService
from api.data.model.Pet import Pet

class PetRepository:
    def __init__(self, dataBaseService: DataBaseService):
        self.db = dataBaseService
        self.collection = "Pets"

    def getPets(self):
        return self.db.getCollection(self.collection)

    def getPetsWhere(self, key, where, value):
        return self.db.getDocumentsWhere(self.collection, key, where, value)

    def getPet(self, idPet):
        return self.db.getDocument(self.collection, idPet)

    def isGetPet(self, idPet):
        return True if self.getPet(idPet) is not None else False

    def addPet(self, pet: Pet):
        return self.db.addDocument(self.collection, pet)

    def updatePet(self, pet: Pet):
        return self.db.updateDocument(self.collection, str(pet._id_), pet)

    def deletePet(self, idPet):
        return self.db.deleteDocument(self.collection, idPet)