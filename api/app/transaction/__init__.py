from flask import Blueprint

# Blueprint Configuration
transaction_bp = Blueprint(
    'transaction_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

from . import routes
