from flask import Blueprint, request, jsonify, make_response
import json
from src import db

sales = Blueprint('sales', __name__)

# @sales.route('')
