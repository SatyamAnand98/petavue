from app import create_app
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    try:
        app.run(port=int(os.getenv("PORT", 8000)), debug=os.getenv("ENV")=="DEBUG")
    except Exception as e:
        pass
