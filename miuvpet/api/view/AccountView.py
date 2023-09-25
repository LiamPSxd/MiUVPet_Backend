from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from api.di.RepositoryModule import account
from api.di.UtilModule import message
from api.data.model.Account import Account
import json

class AccountView(View):
    def __init__(self, repository = account):
        self.repository = repository
        self.message = message

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0, ids = "", condition = ""):
        if request.method == "GET":
            accounts = list()

            if id == 0 and ids == "" and condition == "":
                return self.getAccounts(accounts)
            elif id > 0 and ids == "" and condition == "":
                return self.getAccount(accounts, str(id))
            elif id == 0 and ids != "" and condition == "":
                return self.getAccountsWhereId(accounts, ids)
            elif id == 0 and ids == "" and condition != "":
                condition = condition.split(",")
                return self.getAccountsWhere(accounts, condition[0], condition[1], condition[2])
        else:
            return self.message._lostDB_()

    def getAccounts(self, accounts: list):
        for account in self.repository.getAccounts():
            if account is not None:
                accounts.append(account)

        return self.message.response(accounts)

    def getAccount(self, accounts: list, idAccount):
        account = self.repository.getAccount(idAccount)

        if account is not None:
            accounts.append(account)

        return self.message.response(accounts)

    def getAccountsWhereId(self, accounts: list, ids: str):
        for id in ids.split(","):
            if id != "":
                for account in self.repository.getAccountsWhere("id", "==", int(id)):
                    if account is not None:
                        accounts.append(account)

        return self.message.response(accounts)

    def getAccountsWhere(self, accounts: list, key, where, value):
        if key != "" and where != "":
            for account in self.repository.getAccountsWhere(key, where, value):
                if account is not None:
                    accounts.append(account)

        return self.message.response(accounts)

    def post(self, request):
        if request.method == "POST":
            account = Account.from_dict(json.loads(request.body))

            if account._id_ > 0:
                return self.message._success_() if self.repository.addAccount(account) else self.message._failed_()
            else:
                return self.message._failed_()
        else:
            return self.message._lostDB_()

    def put(self, request, id):
        if request.method == "PUT":
            if self.repository.isGetAccount(str(id)):
                account = Account.from_dict(json.loads(request.body))

                if account._id_ > 0:
                    return self.message._success_() if self.repository.updateAccount(account) else self.message._failed_()
                else:
                    return self.message._failed_()
            else:
                return self.message._noData_()
        else:
            return self.message._lostDB_()

    def delete(self, request, id):
        if request.method == "DELETE":
            if self.repository.isGetAccount(str(id)):
                if id > 0:
                    return self.message._success_() if self.repository.deleteAccount(str(id)) else self.message._failed_()
                else:
                    return self.message._failed_()
            else:
                return self.message._noData_()
        else:
            return self.message._lostDB_()