from api.data.di.NetworkModule import NetworkModule
from firebase_admin.firestore import firestore

class DataBaseService:
    def __init__(self, networkModule: NetworkModule):
        self.db = networkModule.provideDataBase(
            certificate = "miuvpet-firebase-adminsdk.json",
            apiKey = "AIzaSyC9MNPn3iux4qxQtyGCnapcwm-bbsHf4mM",
            authDomain = "miuvpet.firebaseapp.com",
            projectId = "miuvpet",
            storageBucket = "miuvpet.appspot.com",
            messagingSenderId = "935318686128",
            appId = "1:935318686128:web:18ff0aa7264058c3d5ae75",
            measurementId = "G-8F1YF8R262"
        )

    def toDictList(self, data):
        res = list()

        for doc in data:
            res.append(doc.to_dict())

        return res

    def getUltimateId(self, collection):
        data = list()

        if self.db is not None:
            data = self.toDictList(self.db.collection(collection).order_by("id", direction = firestore.Query.DESCENDING).limit(1).stream())

        key = int(data[0]["id"]) if len(data) == 1 else 0

        return key + 1

    def getCollection(self, collection):
        if self.db is not None:
            docs = list(self.db.collection(collection).order_by("id").stream())
            
            return self.toDictList(docs)
        else: return list()

    def getDocumentsWhere(self, collection, key, where, value):
        if self.db is not None:
            docs = list(self.db.collection(collection).where(key, where, value).order_by("id").stream())
        
            return self.toDictList(docs)
        else: return list()

    def getDocument(self, collection, document):
        if self.db is not None:
            doc = self.db.collection(collection).document(document).get()

            if doc.exists: return doc.to_dict()
            else: return None

    def addDocument(self, collection, data):
        if self.db is not None:
            data = data.to_dict()
            data["id"] = self.getUltimateId(collection)
            
            return True if str(self.db.collection(collection).document(str(data["id"])).set(data).update_time) != "" else False
        else: return False

    def updateDocument(self, collection, document, data):
        if self.db is not None:
            return True if str(self.db.collection(collection).document(document).update(data.to_dict()).update_time) != "" else False
        else: return False

    def deleteDocument(self, collection, document):
        if self.db is not None:
            return True if str(self.db.collection(collection).document(document).delete()) != "" else False
        else: return False