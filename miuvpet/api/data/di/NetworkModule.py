import firebase_admin
from firebase_admin import firestore, credentials
from google.cloud.firestore import Client

class NetworkModule:
    def connectionFirebase(self,
                           certificate: str = "",
                           apiKey: str = "",
                           authDomain: str = "",
                           projectId: str = "",
                           storageBucket: str = "",
                           messagingSenderId: str = "",
                           appId: str = "",
                           measurementId: str = "") -> Client | None:
        if not firebase_admin._apps:
            cred = credentials.Certificate(certificate)

            config = {
                "apiKey": apiKey,
                "authDomain": authDomain,
                "projectId": projectId,
                "storageBucket": storageBucket,
                "messagingSenderId": messagingSenderId,
                "appId": appId,
                "measurementId": measurementId
            }

            firebase_admin.initialize_app(cred, config)

        return firestore.client()

    def provideDataBase(self, certificate, apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId, measurementId) -> Client | None:
        return self.connectionFirebase(certificate, apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId, measurementId)