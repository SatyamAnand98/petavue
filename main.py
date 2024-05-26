from flask import Flask
from data_generation import structured_data as CreateData
from flask_cors import CORS

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/create/structured_data", methods=["GET"])
def create_data():
    return CreateData.generate_structured_data(10000, 3)

@app.route("/create/unstructured_data")
def create_unstructured_data():
    return CreateData.generate_unstructured_data(1000)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
