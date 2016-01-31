from time import time, strftime
from datetime import datetime

max_client_records = 120 #number of records allowed per client in their data_entries

class ClientDataManager:
	def __init__(self, json_obj):
		self.data = json_obj;
		
		
	def getData():
		return self.data
	
	
	#Client name is a user-friendly version of the specificied IP addresses name, this enabled easy identification of what machine the data belongs to
	def addIP(self, ip, client_name):
		self.data[ip] = {"client_name": client_name, "data_entries": {}}
	
	
	def getIPData(self, ip):
		return self.data[ip]
	
	
	def addDataEntry(self, ip, data):
		global max_client_records
		
		while len(self.getIPData(ip)) >= max_client_records:
			self.getIPData(ip).pop(0)
		self.getIPData(ip)[datetime.fromtimestamp(time()).strftime("%Y-%m-%dT%H:%M:%S")] = data
		self.getIPData(ip).sort() #Might need to move this to another function (getter?) in case writting to a JSON file rearranges it (maybe use an OrderedDict instead)