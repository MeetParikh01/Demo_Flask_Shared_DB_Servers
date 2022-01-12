import requests
from flask import (
    jsonify,
    request
)
from flask.views import MethodView
from sqlalchemy.orm import sessionmaker
from custom_package.db_handler import handler
from custom_package.models.customers import Customers
from custom_package.managers.customers_managers import CustomersManager


class CustomerView(MethodView):

    def get(self):
        session_cls = sessionmaker(bind=handler.engine, query_cls=CustomersManager)
        session = session_cls()
        x = session.query(Customers).get_customer_data(first_name="Meet").get_first()
        data = {"first_name": x.last_name}
        session.close()
        return jsonify(data)

    def post(self):
        request_json = request.json
        return jsonify({"data": request_json})


class CustomerServiceCallView(MethodView):

    def get(self):
        response = requests.get(url="http://localhost:4000/customer_service2")
        return jsonify(response.json())
