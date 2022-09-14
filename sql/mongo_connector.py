from pymongo import MongoClient

    
class MongoConnector:
    
    def connect(self):
        client = MongoClient("mongodb+srv://admin:admin@stocks.cfrrxev.mongodb.net/?retryWrites=true&w=majority")
        return client
    
    def get_database(self, db):
        client = self.connect() 
        return client[db]   
    
    def get_collection(self, db, collection):
        client = self.connect() 
        return client[db][collection]  
    