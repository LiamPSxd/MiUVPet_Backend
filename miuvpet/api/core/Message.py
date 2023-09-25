from django.http.response import JsonResponse

class Message:
    def _success_(self, data = None):
        if data is None:
            return JsonResponse({"status": "Success"})
        else:
            return JsonResponse({"status": "Success", "data": data})

    def _failed_(self):
        return JsonResponse({"status": "Failed"})

    def _noData_(self):
        return JsonResponse({"status": "Failed", "message": "No se encuentra el dato o datos"})

    def _lostDB_(self):
        return JsonResponse({"status": "Failed", "message": "Se perdio la conexion con la Base de Datos. Por favor, intente más tarde"})

    def response(self, data: list):
        return self._success_(data) if len(data) > 0 else self._noData_()