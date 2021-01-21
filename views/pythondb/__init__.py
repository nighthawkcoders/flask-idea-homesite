"""__init.py__ has responsibility of defining interfaces for blueprint"""
from flask import Blueprint

pythondb_bp = Blueprint(
    'pythondb_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import view
