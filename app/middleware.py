from flask_cors import CORS
from flask import request

def setup_middlewares(app, logger):
    CORS(app)
    
    @app.before_request
    def log_request_info():
        logger.info('Accessed URL: %s', request.url)
        logger.info('Request Headers: %s', request.headers)
        logger.info('Request Body: %s', request.get_data())

    @app.after_request
    def log_response_info(response):
        logger.info('Response Headers: %s', response.headers)
        logger.info('Response Body: %s', f'{response.data[:200]}...')
        return response
