from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30222
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connected Successully.")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data={}):
        if self.database.animals.find(data).count() < 1:
            return {"No Results Found."}
        else:
            return self.database.animals.find(data)  # data should be dictionary  

# Create method to implement the U in CRUD.
    def update(self,data,target={}):
        #data = {"$set": {data}}
        if self.database.animals.find(target).count() > 1:
            self.database.animals.update_many(target,data)
        else:
            self.database.animals.update_one(target, data)
        return self.database.animals.find(target).count()
              

# Create method to implement the D in CRUD.
    def delete(self, data={}):
        if self.database.animals.find(data).count() > 1:
            count = self.database.animals.find(data).count()
            self.database.animals.delete_many(data)
        else:
            count = self.database.animals.find(data).count()
            self.database.animals.delete_one(data)
        return count
                 
        