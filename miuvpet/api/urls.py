from django.urls import path
from api.view.AccountView import AccountView
from api.view.PetView import PetView

account = AccountView.as_view()
pet = PetView.as_view()

urlpatterns = [
    # Accounts
    path('accounts/', account, name = "getAccounts"),
    path('accounts/<int:id>', account, name = "getAccountById"),
    path('accounts/<str:ids>', account, name = "getAccountsWhereId"),
    path('accounts//<str:condition>', account, name = "getAccountsWhere"),

    # Pets
    path('pets/', pet, name = "getPets"),
    path('pets/<int:id>', pet, name = "getPetById"),
    path('pets/<str:ids>', pet, name = "getPetsWhereId"),
    path('pets//<str:condition>', pet, name = "getPetsWhere"),
]