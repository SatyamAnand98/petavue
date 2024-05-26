from flask import request, jsonify
from controllers import data_generation as CreateData
from controllers import summary_report as Report_Generation
from .gpt_comm import generate_result_from_prompt
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
                "response": generate_result_from_prompt(prompt=prompt, gpt_model="gpt-4"),
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
            row_count = 1000
            column_count = 33
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

    @app.route("/summary-report", methods=["GET"])
    def summary_report():
        try:
            current_dir = os.getcwd()
            file_path = os.path.join(current_dir, 'files/petavue_structured_data_processed.xlsx')
            Report_Generation.report()
            return {
                "response": f'Summary Report Generated. Please check the file {file_path}',
                "status": "success"
            }
        except Exception as e:
            logger.error(e)
            return {
                "response": str(e),
                "status": "error"
            }