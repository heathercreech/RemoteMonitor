import requests


def sendClientRequest(request="update"):
	return requests.get(getClientIP()+ "/" + request).content;