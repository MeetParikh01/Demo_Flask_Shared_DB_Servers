from flask import Blueprint
from app.customers.views import (
    CustomerView,
    CustomerServiceCallView
)

customers_routes = Blueprint('customer_routes', __name__)

customers_routes.add_url_rule('/customer', view_func=CustomerView.as_view('customer'))
customers_routes.add_url_rule('/call_customer2', view_func=CustomerServiceCallView.as_view('call_customer2'))

