import flask
import json
from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route("/", methods = ["GET"])

def main():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=8000)
    
