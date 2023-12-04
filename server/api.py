from flask import Flask, jsonify, request
from flasgger import swag_from

from firebase_admin import auth

from .auth import authenticate_request
from .controllers.sales_controller import SalesController

app = Flask(__name__)


@app.route("/", methods=["GET"])
@swag_from("./docs/celes-api-docs.yml")
def index():
    return jsonify({"status": 200, "response": "ok"})


@app.route("/login", methods=["POST"])
@swag_from("./docs/celes-api-docs.yml")
def login():
    try:
        email = request.json["email"]
        password = request.json["password"]

        user = auth.get_user_by_email(email)

        custom_token = auth.create_custom_token(user.uid)

        return jsonify({"customToken": custom_token.decode()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 401


@app.route("/getSalesByEmployee", methods=["GET"])
@swag_from("./docs/celes-api-docs.yml")
@authenticate_request
def get_sales_by_employee():
    try:
        employee_id = request.args.get("employee_id")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        date_range = (start_date, end_date)

        response = SalesController.get_sales_by_employee(employee_id, date_range)
        return jsonify({"response": response}), 200

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500


@app.route("/getSalesByProduct", methods=["GET"])
@swag_from("./docs/celes-api-docs.yml")
@authenticate_request
def get_sales_by_product():
    try:
        product_id = request.args.get("product_id")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        date_range = (start_date, end_date)

        response = SalesController.get_sales_by_product(product_id, date_range)
        return jsonify({"response": response}), 200

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500


@app.route("/getSalesByStore", methods=["GET"])
@swag_from("./docs/celes-api-docs.yml")
@authenticate_request
def get_sales_by_store():
    try:
        store_id = request.args.get("store_id")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        date_range = (start_date, end_date)

        response = SalesController.get_sales_by_store(store_id, date_range)
        return jsonify({"response": response}), 200

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500


@app.route("/getSalesInformationByStore", methods=["GET"])
@swag_from("./docs/celes-api-docs.yml")
@authenticate_request
def get_sales_information_by_store():
    try:
        store_id = request.args.get("store_id")
        response = SalesController.get_total_and_mean_sale_by_store(store_id)
        return jsonify({"response": response}), 200

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500


@app.route("/getSalesInformationByProduct", methods=["GET"])
@swag_from("./docs/celes-api-docs.yml")
@authenticate_request
def get_sales_information_by_product():
    try:
        product_id = request.args.get("store_id")
        response = SalesController.get_total_and_mean_sale_by_employee(product_id)
        return jsonify({"response": response}), 200

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500


@app.route("/getSalesInformationByEmployee", methods=["GET"])
@swag_from("./docs/celes-api-docs.yml")
@authenticate_request
def get_sales_information_by_employee():
    try:
        employee_id = request.args.get("employee_id")

        response = SalesController.get_total_and_mean_sale_by_employee(employee_id)
        return jsonify({"response": response}), 200

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500
