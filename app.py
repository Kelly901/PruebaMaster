from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])

def login():

	if request.method == 'GET':


		return "HOLA MUNDO CRUEL"		
		
	
	

@app.route("/")
def index():
	
	return "F"

if __name__ == "__main__":
	app.run(threaded=True,port=8000,debug=True)
