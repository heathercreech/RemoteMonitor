import requests
import json

def sendClientRequest(ip, call="update"):
	encoded_json_data = requests.get(ip + "/" + call).content
	return json.loads(str(encoded_json_data.decode("utf-8")));