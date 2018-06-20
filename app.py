from flask import Flask, request,jsonify
import requests
import json
import AnalyzeUser as au
import analysisResults as ar
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/analyse",methods=['POST'])
    
def analysis():
    user = {
        "_id" : request.form.get("_id"),
        "username": request.form.get("username"),
        "fullName" : request.form.get("fullName"),
        "private": int(request.form.get("private")),
        "verified": int(request.form.get("verified")),
        "profilePicture": request.form.get("profilePicture"),
        "counts": {"Followers":int(request.form.get("Followers")),
                   "Following":int(request.form.get("Following")),
                   "UserTags" : int(request.form.get("UserTags")),
                   "Media": int(request.form.get("countsm"))
                   },
        "bio": request.form.get("bio"),
        "city": request.form.get("city"),
        "publicEmail": request.form.get("publicEmail"),
        "birthday": request.form.get("birthday"),
        "media" : request.form.getlist("media[]")
        }
    #user = json.loads(data.text)
    userToAnalyze = au.UserAnalyze(user['_id'], user['fullName'], user['username'], user['counts']['Followers'], user['counts']['Following'], user['counts']['Media'], user['counts']['UserTags'], user['bio'], user['private'], user['media'], user['profilePicture'])
    userToAnalyze.analyze()
    if userToAnalyze.isSuspicious():
        sendBackToDB = ar.analysisResults(userToAnalyze, True)
    else:
        sendBackToDB = ar.analysisResults(userToAnalyze, False)
    #pushDataToDB(sendBackToDB.__dict__, sendBackToDB.userID)
    UserFeature = [sendBackToDB.isPrivate, sendBackToDB.postVSfollowers, sendBackToDB.followingVSfollowers, sendBackToDB.suspiciousName, sendBackToDB.emptyProfile, sendBackToDB.googleSRnumOfLinks, sendBackToDB.googleSRnumOfPages, sendBackToDB.numOfUserTags, sendBackToDB.numOfMedia, sendBackToDB.numOfFollowing, sendBackToDB.numOfFollowers]
    UserFeature = np.asarray(UserFeature)
    filename = 'finalized_model.sav'
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    # load the score from disk
    scoreName = 'score_model.sav'
    loaded_score = pickle.load(open(scoreName, 'rb'))
    
    result = loaded_model.predict(UserFeature.reshape(1,-1))
    
    return str(result[0]) + '&' + str(loaded_score)
    
if __name__ == "__main__":
    app.run()
