from flask import Blueprint
from app.customers.views import CustomerView

customers_routes = Blueprint('customer_routes', __name__)

customers_routes.add_url_rule('/customer_service2', view_func=CustomerView.as_view('customer'))
