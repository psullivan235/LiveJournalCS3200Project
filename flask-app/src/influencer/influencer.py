from flask import Blueprint, request, jsonify, make_response
import json
from src import db

influencer = Blueprint('influencer', __name__)


@influencer.route('/follows/<FollowerUserID>', methods=['GET'])
def get_influencers_follows(FollowerUserID):
    query = f'''
            SELECT *
            FROM Follows
            WHERE FollowerUserID = {FollowerUserID}
            '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@influencer.route('/GroupMemberships/<userID>', methods=['GET'])
def get_influencers_groups(userID):
    query = f'''
            SELECT GroupID
            FROM GroupMemberships
            WHERE userID = {userID}
            '''

    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@influencer.route('/posts/<userID>/day', methods=['GET'])
def get_influencers_posts(userID):
    formData = request.json
    day = formData['day'] # Day in "YYYY-MM-DD"
    beginTime = "00:00:00"
    endTime = "23:59:59"
    beginDateTime = f"{day} {beginTime}"
    endDateTime = f"{day} {endTime}"
    query = f'''
            SELECT *
            FROM Posts
            WHERE userID = {userID} AND (PostedOn >= '{beginDateTime}')
                AND (PostedOn <= '{endDateTime}')
            '''

    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []
    column_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()

    for row in data:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@influencer.route('/posts/<userID>/day/reaction', methods=['GET'])
def get_influencers_posts_reactions(userID):
    formData = request.json
    day = formData['day'] # Day in "YYYY-MM-DD"
    beginTime = "00:00:00"
    endTime = "23:59:59"
    beginDateTime = f"{day} {beginTime}"
    endDateTime = f"{day} {endTime}"

    query = f'''
            SELECT Reaction
            FROM Posts JOIN PostReactions USING (PostID)
            WHERE Posts.UserID = {userID}
                AND (PostedOn >= '{beginDateTime}') AND (PostedOn <= '{endDateTime}')
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
def create_follows(InfluencerUserID, FollowerUserID):
    formData = request.json
    Friend = formData['Friend']

    query = f"INSERT into Follows (Friend, InfluencerUserID, FollowerUserID) VALUES ({Friend}, {InfluencerUserID}, {FollowerUserID})"

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"


@influencer.route('/follows/<InfluencerUserID>/<FollowerUserID>', methods=['DELETE'])
def delete_follows(InfluencerUserID, FollowerUserID):
    query = f'''
            DELETE FROM Follows
            WHERE InfluencerUserID = {InfluencerUserID} AND FollowerUserID = {FollowerUserID}
            '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"


@influencer.route('/posts/<UserID>/day', methods=['POST'])
def create_posts(UserID):
    formData = request.json
    day = formData['day']
    PostedOn = f"{day} 00:00:00"
    Content = formData['Content']


    query = f"INSERT into Posts (Content, PostedOn, UserID) VALUES ('{Content}', '{PostedOn}', {UserID})"

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"


@influencer.route('/posts/<UserID>/day', methods=['PUT'])
def put_posts(UserID):
    formData = request.json
    day = formData['day'] # Day in "YYYY-MM-DD"
    beginTime = "00:00:00"
    endTime = "23:59:59"
    beginDateTime = f"{day} {beginTime}"
    endDateTime = f"{day} {endTime}"
    Likes = formData['Likes']
    Views = formData['Views']
    Content = formData['Content']

    query = f'''
        UPDATE Posts
        SET Likes = '{Likes}', Views = '{Views}', Content = '{Content}'
        WHERE UserID = {UserID} AND (PostedOn >= '{beginDateTime}') AND (PostedOn <= '{endDateTime}')
        '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Success"
