from flask import request, jsonify
from controllers import data_generation as CreateData
from controllers import summary_report2 as Report_Generation
from .gpt_comm import openAI_API_Prompt
from store.logging import configure_logger
import os

logger = configure_logger()

def setup_routes(app):
    @app.route('/')
    def hello_world():
        try:
            return{
                "msg": 'Hello, World!',
                "status": "success"
            }
        except Exception as e:
            logger.error(e)
            return {
                "msg": str(e),
                "status": "error"
            }

    @app.route("/chat", methods=["POST"])
    def generate_result():
        try:
            data = request.get_json()
            prompt = data["prompt"]
            return {
                "response": openAI_API_Prompt(prompt=prompt, gpt_model="gpt-4"),
                "status": "success"
            }
        except Exception as e:
            logger.error(e)
            return {
                "response": str(e),
                "status": "error"
            }

    @app.route("/create/structured_data", methods=["GET"])
    def create_data():
        try:
            row_count = int(request.args.get("row")) or 1000
            column_count = int(request.args.get("column")) or 33

            return {
                "response": CreateData.generate_structured_data(row_count, column_count),
                "status": "success"
            }
        except Exception as e:
            logger.error(e)
            return {
                "response": str(e),
                "status": "error"
            }

    @app.route("/create/unstructured_data")
    def create_unstructured_data():
        try:
            row_count = 1300
            return CreateData.generate_unstructured_data(row_count)
        except Exception as e:
            logger.error(e)
            return {
                "response": str(e),
                "status": "error"
            }

    @app.route("/process-data", methods=["POST"])
    def process_data():
        try:
            data = request.get_json()
            prompt = data["prompt"]
            return {
                "response": Report_Generation.prompt_processing(prompt),
                "status": "success"
            }
        except Exception as e:
            logger.error(e)
            return {
                "response": "Oops!! Something wrong happened! Please try again",
                "error": True
            }