from api.data.network.DataBaseService import DataBaseService
from api.data.di.NetworkModule import NetworkModule
from api.core.Message import Message

dataBaseService = DataBaseService(NetworkModule())
message = Message()