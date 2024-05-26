from flask import Flask
from dotenv import load_dotenv
from .routes import setup_routes
from .middleware import setup_middlewares
from store.logging import configure_logger

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    logger = configure_logger()
    
    setup_middlewares(app, logger)
    setup_routes(app)
    
    return app
