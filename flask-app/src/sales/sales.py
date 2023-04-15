from flask import Blueprint, request, jsonify, make_response
import json
from src import db

sales = Blueprint('sales', __name__)

@sales.route('/advertisements', methods=['GET'])
def get_ads():
    query = '''
            SELECT *
            FROM Advertisements
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
