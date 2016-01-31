import hashlib
import json


default_json_object = {"users": {}, "settings": {"next_id": 0, "deleted_ids": []}}


def hashPassword(password):
	return hashlib.sha256(password).digest()


#handles adding users, checking passwords, and getting the user data out of it
class RMUserDatabase:
	
	def __init__(self, database_filepath):
		self.filepath = database_filepath
		
		db_file_data = json.loads(self.loadUserData())
		
		self.users = db_file_data["users"]
		self.settings = db_file_data["settings"]
		
	
	#enable the use of the with keyword (removes the need to call saveUserData() manually)
	def __enter__(self):
		return self
	
	
	def __exit__(self, exc_type, exc_value, traceback):
		self.saveUserData()

	
	def loadUserData(self):
		global default_json_object
		
		try:
			database_text = ""
			with open(self.filepath) as db_file:
				database_text = db_file.readline().rstrip("\n")
			return database_text
		except FileNotFoundError:
			print("File '", self.filepath, "' does not exist.")
			return json.dumps(default_json_object)
		
		
	def saveUserData(self):
		with open(self.filepath, "w") as db_file:
			db_file.write(json.dumps({"users": self.users, "settings": self.settings}))
	
	
	#Utility methods
	def checkPassword(self, username, password):
		if self.getUserData(username)["password_hash"] == hashPassword(password.encode("utf-16")).decode("utf-16"):
			return True
		return False

		
	def getNextId(self):
		if len(self.settings["deleted_ids"]) > 0:
			return self.settings["deleted_ids"].pop()
		else:
			self.settings["next_id"] += 1
			return self.settings["next_id"]-1	
	
	
	#Getters
	def getUserData(self, username):
		try:
			return self.users[username]
		except KeyError:
			print("Error: user is not in the database")
			return {}
	
	
	def getClientIPs(self, username):
		return self.getUserData(username)["ip_addresses"]
	
	
	#Setters
	def setUserData(self, username, data):
		self.users.update({username: data})
	
	
	#Database modification methods
	def addUser(self, username, ip_addresses, password):
		self.setUserData(username, {"id": self.getNextId(), "ip_addresses": ip_addresses, "password_hash": hashPassword(password.encode("utf-16")).decode("utf-16")})
		
	
	def removeUser(self, username):
		user_data = self.users.pop(username)
		self.settings["deleted_ids"].append(user_data["id"])
		
	
	def addIPAddress(self, username, ip):
		self.getClientIPs(username).append(ip)