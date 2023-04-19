from flask import Blueprint, request, jsonify, make_response, current_app
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

@sales.route('/advertisements', methods=['POST'])
def create_ad():
    formData = request.json
    adName = formData['Name']
    adDescription = formData['Description']
    adContent = formData['Content']
    adCompanyID = formData['CompanyID']

    query = f"INSERT into Advertisements (Name, Description, Content, CompanyID) VALUES ('{adName}', '{adDescription}', '{adContent}', {adCompanyID})"

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"

@sales.route('/advertisements/<AdID>', methods=['GET'])
def get_ad(AdID):
    query = f'''
            SELECT *
            FROM Advertisements
            WHERE AdID = {AdID}
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@sales.route('/advertisements/<AdID>', methods=['PUT'])
def update_ad(AdID):
    formData = request.json
    adName = formData['Name']
    adDescription = formData['Description']
    adContent = formData['Content']

    query = f'''
        UPDATE Advertisements
        SET Name = '{adName}', Description = '{adDescription}', Content = '{adContent}'
        WHERE AdID = {AdID}
        '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"

@sales.route('/advertisements/<AdID>', methods=['DELETE'])
def delete_ad(AdID):
    query = f'''
            DELETE FROM Advertisements
            WHERE AdID = {AdID}
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"

@sales.route('/sponsorships/<CompanyID>', methods=['GET'])
def get_sponsorships(CompanyID):
    query = f'''
            SELECT *
            FROM Sponsorship
            WHERE CompanyID = {CompanyID}
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@sales.route('/sponsorships/<CompanyID>', methods=['POST'])
def create_sponsorship(CompanyID):
    formData = request.json
    UserID = formData['UserID']
    Compensation = formData['Compensation']

    query = f"INSERT into Sponsorship (CompanyID, UserID, Compensation) VALUES ({CompanyID}, {UserID}, '{Compensation}')"

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"

@sales.route('/user/active/day', methods=['GET'])
def get_active_users():
    formData = request.json
    day = formData['day'] # Day in "YYYY-MM-DD"
    beginTime = "00:00:00"
    endTime = "23:59:59"
    beginDateTime = f"{day} {beginTime}"
    endDateTime = f"{day} {endTime}"
    query = f'''
            SELECT COUNT(*) AS count
            FROM Users JOIN UserMetadata USING (UserID)
            WHERE (TimeOnSite >= '{beginDateTime}') AND (TimeOnSite <= '{endDateTime}')
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@sales.route('/posts/postsPerDay', methods=['GET'])
def get_posts_per_day():
    formData = request.json
    day = formData['day'] # Day in "YYYY-MM-DD"
    beginTime = "00:00:00"
    endTime = "23:59:59"
    beginDateTime = f"{day} {beginTime}"
    endDateTime = f"{day} {endTime}"
    query = f'''
            SELECT COUNT(*) AS count
            FROM Posts
            WHERE (PostedOn >= '{beginDateTime}') AND (PostedOn <= '{endDateTime}')
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@sales.route('/posts/totalViews/day', methods=['GET'])
def get_total_views_per_day():
    formData = request.json
    day = formData['day'] # Day in "YYYY-MM-DD"
    beginTime = "00:00:00"
    endTime = "23:59:59"
    beginDateTime = f"{day} {beginTime}"
    endDateTime = f"{day} {endTime}"
    query = f'''
            SELECT SUM(Views) AS totalViews
            FROM Posts
            WHERE (PostedOn >= '{beginDateTime}') AND (PostedOn <= '{endDateTime}')
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        # Sum of nothing will not return 0, manually overwriting
        if (row == (None,)):
            row = (0,)
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
