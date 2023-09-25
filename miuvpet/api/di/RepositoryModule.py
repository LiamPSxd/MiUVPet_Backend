from api.data.repository.AccountRepository import AccountRepository
from api.data.repository.PetRepository import PetRepository
from api.di.UtilModule import dataBaseService

account = AccountRepository(dataBaseService)
pet = PetRepository(dataBaseService)