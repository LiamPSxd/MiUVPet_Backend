from api.data.network.DataBaseService import DataBaseService
from api.data.model.Account import Account

class AccountRepository:
    def __init__(self, dataBaseService: DataBaseService):
        self.db = dataBaseService
        self.collection = "Accounts"

    def getAccounts(self):
        return self.db.getCollection(self.collection)

    def getAccountsWhere(self, key, where, value):
        return self.db.getDocumentsWhere(self.collection, key, where, value)

    def getAccount(self, idAccount):
        return self.db.getDocument(self.collection, idAccount)

    def isGetAccount(self, idAccount):
        return True if self.getAccount(idAccount) is not None else False

    def addAccount(self, account: Account):
        return self.db.addDocument(self.collection, account)

    def updateAccount(self, account: Account):
        return self.db.updateDocument(self.collection, str(account._id_), account)

    def deleteAccount(self, idAccount):
        return self.db.deleteDocument(self.collection, idAccount)