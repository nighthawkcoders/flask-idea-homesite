"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

restapi_bp = Blueprint(
    'restapi_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view
