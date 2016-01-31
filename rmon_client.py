from flask import Flask
import json
from rmon_info import packAllInfo

app = Flask(__name__)


	
@app.route('/update')
def update():
	return json.dumps(packAllInfo())

	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001)