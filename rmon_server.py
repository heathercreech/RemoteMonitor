from os import urandom
from flask import Flask, session, escape, request, redirect, url_for
from flask import render_template
import json
import threading
from rmon_database import RMUserDatabase
from rmon_requests import sendClientRequest


app = Flask(__name__)


auto_update_seconds = 5


@app.route('/login', methods=['GET', 'POST'])
def login():
	global database
	
	if request.method == "POST":
		if database.checkPassword(request.form["username"], request.form["password"]):
			session["username"] = request.form["username"]
			return redirect(url_for("home"))
		return "Login failed"
	return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
	global database
	
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		confirm = request.form["confirm"]
		
		if password == confirm and len(password) >= 6:
			if username not in database.users:
				database.addUser(username, [], password)
				return redirect(url_for("login"))
	return render_template("register.html")
	

@app.route("/help")
def help():
	pass
	
	
#updates the Jinja env globals with a function name
def updateJinja(func):
	app.jinja_env.globals[func.__name__] = func


#temporary function to get data into the charts
def temp():
	return [1,60,11,25,30,9]

	
def getSecretKey(filepath):
	try:
		with open(filepath) as sk_file:
			return sk_file.readline()
	except FileNotFoundError:
		generated_key = str(urandom(50))
		with open(filepath, "w") as sk_file:
			sk_file.write(generated_key)
			return generated_key


def recurringUpdate(ip_address):
	database.client_data.addDataEntry(ip_address, sendClientRequest(ip_address))
	print(database.client_data.getIPData(ip_address)["data_entries"])
	threading.Timer(auto_update_seconds, recurringUpdate, args=(ip_address,)).start()
	
	
@app.route('/')
def home():
	if "username" in session:
		for ip in database.getClientIPs(session["username"]):
			recurringUpdate(ip)
			pass
		return render_template("monitor.html")
	else:
		return redirect(url_for("login"))


	
if __name__ == "__main__":
	
	database_filename = "database.json"
	database = {}
	
	app.secret_key = getSecretKey("secret_key.cfg")
	
	updateJinja(temp)
	database = RMUserDatabase(database_filename)
	
	app.run(debug=True)
	database.saveUserData()