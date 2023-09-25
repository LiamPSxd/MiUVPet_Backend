from django.http.response import JsonResponse
from api.di.UtilModule import dataBaseService as db
from api.data.model.Account import Account
from api.data.model.Pet import Pet

def index(request):
    if request.method == "GET":
        res = list()

        # Obtener una Colección de datos
        # for i in db.getCollection("Accounts"):
        #     res.append(i)

        # Obtener un(os) Documento(s) a partir de una condición
        # for i in db.getDocumentsWhere("1", "id", "==", 2):
        #     res.append(i)

        # Obtener un Documento
        # for key, value in db.getDocument("1", "1").items():
        #     if value != None:
        #         res.append(value)

        # Agregar un Documento
        # db.addDocument("Accounts", Account(name = "Liam", email = "liam@correo.com", password = "liam"))
        # db.addDocument("Pets", Pet(name = "Liam", nickname = "lps"))

        # Modificar un Documento
        # pet = Pet(id = 1, name = "Liam", nickname = "lps")
        # db.updateDocument("Pets", str(pet._id_), pet)

        # Eliminar un Documento
        # db.deleteDocument("Accounts", "3")

        # Retornos
        # return JsonResponse({"Success": "OK"})
        return JsonResponse({"Success": res})