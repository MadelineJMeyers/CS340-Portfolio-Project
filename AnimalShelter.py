from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):

	""" CRUD operations for Animal Collection in MongoDB """

	def __init__(self, usr, pwd):

		#Connection Variables

		USER = usr
		PASS = pwd
		HOST = 'nv-desktop-services.apporto.com' 
		PORT = 32808
		DB = 'AAC'
		COL = 'animals'

		#Initialize Connection

		self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
		self.database = self.client['%s' % (DB)]
		self.collection = self.database['%s' % (COL)]

	# Create Function
	def create(self,data):
		if data is not None:
			insert = self.database.animals.insert_one(data) #Expects Dictionary to insert
			if insert != 0:
				print(insert)
				return True
			else:
				return False
		else:
			raise Exception("Nothing to save, because data parameter is empty")

	# Read Function
	def read(self, data=None):
		if data:
			returnData = self.database.animals.find(data, {"_id": False}) # Expects Dictionary to query
		else:
			returnData = self.database.animals.find({}, {"id" : False})
		return list(returnData)
		
	# Update Function
	def update(self, orgData, newData):
		updateCount = 0
		if orgData and newData is not None:
			update = self.database.animals.update_many(orgData, {"$set": newData}) # Expects 2 Dictionaries to Update with original data and new data to set
			if update != 0:
				print(update)
				updateCount += 1
		else:
			raise Exception("Nothing to update, because data parameter is empty")
		return updateCount
    
	# Delete Function
	def delete(self, data):
		deletedCount = 0
		if data is not None:
			data_to_delete = self.database.animals.delete_many(data)
			if data_to_delete != 0:
				print(data_to_delete)
				deletedCount += 1
		else:
			raise Exception("Nothing to delete, because data parameter is empty")
		return deletedCount
