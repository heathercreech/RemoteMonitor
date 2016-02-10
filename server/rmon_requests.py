import json

import requests


def sendClientRequest(ip, call="update"):
	encoded_json_data = requests.get("http://" + ip + "/" + call).content
	return json.loads(str(encoded_json_data.decode("utf-8")));