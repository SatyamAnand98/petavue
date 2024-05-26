from flask import Flask
from data_generation import structured_data as CreateData
from flask_cors import CORS

from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

@app.route('/')
def hello_world():
    """
    A simple function that returns a greeting message.

    Returns:
        str: The greeting message.
    """
    return 'Hello, World!'

@app.route("/create/structured_data", methods=["GET"])
def create_data():
    """
    Generate structured data.

    This function generates structured data with the specified number of rows and columns.

    Parameters:
    - row_count (int): The number of rows in the generated data.
    - column_count (int): The number of columns in the generated data.

    Returns:
    - str: The generated structured data.
    """
    # Default values for row_count and column_count
    row_count = 1000
    column_count = 3
    return CreateData.generate_structured_data(row_count, column_count)

@app.route("/create/unstructured_data")
def create_unstructured_data():
    """
    Generate unstructured data.

    This function generates unstructured data with the specified number of rows.

    Parameters:
    - row_count (int): The number of rows to generate.

    Returns:
    - str: The generated unstructured data.
    """
    # Default value for row_count
    row_count = 1300
    return CreateData.generate_unstructured_data(row_count)

if __name__ == '__main__':
    # Run the Flask application
    # Set port to 8000 and enable debug mode for testing and rerun the code on file change
    app.run(port=8000, debug=True)
