import requests 
import json
import AnalyzeUser as au
import analysisResults as ar

def pushDataToDB(analysisResults, userID):
    toPush = {}
    #analysisResults = {}
    #analysisResults['test'] = 'Blabla'
    toPush['$push'] = analysisResults
    jsonToPush = json.dumps(toPush)
    #print (jsonToPush)
    headers = {'Content-type' : 'application/json'}
    r = requests.put('https://api.mlab.com/api/1/databases/analysis/collections/users?apiKey=tvG8BMjzxtNwm3fRgQv4LNbcF2IIeWWc&q={"_id":"' + userID + '"}',
                     data = jsonToPush, headers=headers)
    #print(r.text)
    return;

<<<<<<< HEAD
=======
'''
#get data on user already exist
r = requests.get('https://api.mlab.com/api/1/databases/analysis/collections/users?apiKey=tvG8BMjzxtNwm3fRgQv4LNbcF2IIeWWc&q={"_id":"4226040806"}')
print(r.text)
'''
#tmpp = au.UserAnalyze()
>>>>>>> 00c1f5a648403a69a4147115062a407e30087dee

jsonData = requests.get('https://api.mlab.com/api/1/databases/analysis/collections/users?q={%22trackingResults%22:{%22$exists%22:false}}&apiKey=tvG8BMjzxtNwm3fRgQv4LNbcF2IIeWWc')
#print(jsonData.text)
jsonToPython = json.loads(jsonData.text)
<<<<<<< HEAD
#del jsonToPython[0]
=======
del jsonToPython[0]
>>>>>>> 00c1f5a648403a69a4147115062a407e30087dee
usersToAnalyze = []
for user in jsonToPython:
    usersToAnalyze.append(au.UserAnalyze(user['_id'], user['fullName'], user['username'], user['counts']['Followers'], user['counts']['Following'], user['counts']['Media'], user['counts']['UserTags'], user['bio'], user['private'], user['media'], user['profilePicture']))

<<<<<<< HEAD
=======
'''
for user in usersToAnalyze:
    print(user.userDetails())
'''
>>>>>>> 00c1f5a648403a69a4147115062a407e30087dee
suspiciousUsers = []
sendBackToDB = []
for user in usersToAnalyze:
    user.analyze()
    if user.isSuspicious():
        suspiciousUsers.append(user)
        sendBackToDB.append(ar.analysisResults(user, True))
    else:
        sendBackToDB.append(ar.analysisResults(user, False))
        
for userToPush in sendBackToDB:
    pushDataToDB(userToPush.__dict__, userToPush.userID)
<<<<<<< HEAD

=======
>>>>>>> 00c1f5a648403a69a4147115062a407e30087dee
