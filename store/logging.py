import logging
import os
from dotenv import load_dotenv

load_dotenv()

def configure_logger():
    level = logging.DEBUG

    env_mode = os.getenv("ENV")
    if env_mode == "PRODUCTION":
        level = logging.INFO
    elif env_mode == "TESTING":
        level = logging.ERROR
    elif env_mode in ["DEVELOPMENT", "DEBUG"]:
        level = logging.DEBUG

    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # Check if the logger already has handlers
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler('./files/logs/app.log')
        file_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
