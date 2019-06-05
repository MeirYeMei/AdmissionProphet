from pymongo import MongoClient
import pymongo
uri = "mongodb://localhost:27017"
class DataBaseManager(object):
    def __init__(self,uri = uri):
        #Todo: add more documents here if needed
        self.client = MongoClient(uri)
        self.application_result = self.client['grad_application_result']['application_result']

    # Todo: decide schema here?
