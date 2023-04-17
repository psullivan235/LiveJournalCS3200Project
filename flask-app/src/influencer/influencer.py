from flask import Blueprint, request, jsonify, make_response
import json
from src import db

influencer = Blueprint('influencer', __name__)

@influencer.route('/follows/<UserID>', methods=['GET'])
def get_influencers(UserID):
    query = f'''
            SELECT *
            FROM Follows
            WHERE UserID = {UserID}
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@influencer.route('/groups/<UserID>', methods=['GET'])
def get_influencers(UserID):
    query = f'''
            SELECT *
            FROM Groups
            WHERE UserID = {UserID}
            '''

    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@influencer.route('/follows/<InfluencerUserID>/<FollowerUserID>', methods=['POST'])
def create_sponsorship(InfluencerUserID, FollowerUserID):
    formData = request.json
    Friend = formData['Friend']

    query = f"INSERT into Follows (Friend, InfluencerUserID, FollowerUserID) VALUES ({Friend}, {InfluencerUserID}, '{FollowerUserID}')"

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"


@influencer.route('/follows/<InfluencerUserID>/<FollowerUserID>', methods=['DELETE'])
def delete_ad(InfluencerUserID, FollowerUserID):
    query = f'''
            DELETE FROM Follows
            WHERE InfluencerUserID = {InfluencerUserID} AND FollowerUserID = {FollowerUserID}
            '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"