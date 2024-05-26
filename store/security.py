from dotenv import load_dotenv
import os

load_dotenv()

def add_security(app):
    """
    Adds security configurations to the Flask app.

    Parameters:
    - app: The Flask app object.

    Configuration Options:
    - SECRET_KEY: The secret key used for cryptographic operations.
    - DEBUG: Sets the app to debug mode based on the environment configuration.
    - TESTING: Sets the app to testing mode.
    - WTF_CSRF_ENABLED: Enables or disables CSRF protection.
    - WTF_CSRF_CHECK_DEFAULT: Enables or disables CSRF protection.
    - WTF_CSRF_TIME_LIMIT: The time limit for CSRF protection.
    - WTF_CSRF_METHODS: The HTTP methods allowed for CSRF protection.
    - WTF_CSRF_HEADERS: The headers used for CSRF protection.
    - WTF_CSRF_SSL_STRICT: Enables or disables strict SSL checking for CSRF protection.
    - WTF_CSRF_SSL_INSECURE: Enables or disables SSL checking for CSRF protection.
    - WTF_CSRF_SSL_CHECK: Enables or disables SSL checking for CSRF protection.
    - WTF_CSRF_SSL_REDIRECT: Enables or disables SSL redirection for CSRF protection.
    - WTF_CSRF_SSL_REDIRECT_CODE: The HTTP status code for SSL redirection.
    - WTF_CSRF_SSL_REDIRECT_METHOD: The HTTP method for SSL redirection.
    - WTF_CSRF_SSL_REDIRECT_MESSAGE: The message displayed during SSL redirection.
    - WTF_CSRF_SSL_REDIRECT_TIMEOUT: The timeout for SSL redirection.
    - WTF_CSRF_SSL_REDIRECT_WARNING: Enables or disables warning message for SSL redirection.
    - WTF_CSRF_SSL_REDIRECT_WARNING_MESSAGE: The warning message displayed during SSL redirection.
    - WTF_CSRF_SSL_REDIRECT_WARNING_TIMEOUT: The timeout for the warning message during SSL redirection.
    - WTF_CSRF_SSL_REDIRECT_WARNING_CODE: The HTTP status code for the warning message during SSL redirection.
    - WTF_CSRF_SSL_REDIRECT_WARNING_METHOD: The HTTP method for the warning message during SSL redirection.
    """
    app.config['SECRET_KEY'] = 'secret'                                      
    app.config['DEBUG'] = os.getenv("ENV") == "DEBUG"
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['WTF_CSRF_CHECK_DEFAULT'] = False
    app.config['WTF_CSRF_TIME_LIMIT'] = 3600
    app.config['WTF_CSRF_METHODS'] = ['POST', 'PUT', 'PATCH', 'DELETE']
    app.config['WTF_CSRF_HEADERS'] = ['X-CSRFToken', 'X-CSRF-Token']
    app.config['WTF_CSRF_SSL_STRICT'] = True
    app.config['WTF_CSRF_SSL_INSECURE'] = False
    app.config['WTF_CSRF_SSL_CHECK'] = True
    app.config['WTF_CSRF_SSL_REDIRECT'] = True
    app.config['WTF_CSRF_SSL_REDIRECT_CODE'] = 301
    app.config['WTF_CSRF_SSL_REDIRECT_METHOD'] = 'GET'
    app.config['WTF_CSRF_SSL_REDIRECT_MESSAGE'] = 'Please use HTTPS'
    app.config['WTF_CSRF_SSL_REDIRECT_TIMEOUT'] = 5
    app.config['WTF_CSRF_SSL_REDIRECT_WARNING'] = True
    app.config['WTF_CSRF_SSL_REDIRECT_WARNING_MESSAGE'] = 'Please use HTTPS'
    app.config['WTF_CSRF_SSL_REDIRECT_WARNING_TIMEOUT'] = 5
    app.config['WTF_CSRF_SSL_REDIRECT_WARNING_CODE'] = 301
    app.config['WTF_CSRF_SSL_REDIRECT_WARNING_METHOD'] = 'GET'