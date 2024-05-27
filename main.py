from app import create_app
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(port=os.getenv("PORT"), debug=os.getenv("ENV")=="DEBUG")
    except Exception as e:
        pass
