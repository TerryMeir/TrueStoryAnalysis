import requests 
import json
import AnalyzeUser as au

def pushDataToDB(analysisResults):
    toPush = {}
    #analysisResults = {}
    #analysisResults['test'] = 'Blabla'
    toPush['$push'] = analysisResults
    jsonToPush = json.dumps(toPush)
    #print (jsonToPush)
    headers = {'Content-type' : 'application/json'}
    r = requests.put('https://api.mlab.com/api/1/databases/analysis/collections/users?apiKey=tvG8BMjzxtNwm3fRgQv4LNbcF2IIeWWc&q={"_id":"4226040806"}',
                     data = jsonToPush, headers=headers)
    print(r.text)
    return;

'''
#get data on user already exist
r = requests.get('https://api.mlab.com/api/1/databases/analysis/collections/users?apiKey=tvG8BMjzxtNwm3fRgQv4LNbcF2IIeWWc&q={"_id":"4226040806"}')
print(r.text)
'''
#tmpp = au.UserAnalyze()

jsonData = requests.get('https://api.mlab.com/api/1/databases/analysis/collections/users?apiKey=tvG8BMjzxtNwm3fRgQv4LNbcF2IIeWWc')
#print(jsonData.text)
jsonToPython = json.loads(jsonData.text)
del jsonToPython[0]
usersToAnalyze = []
for user in jsonToPython:
    usersToAnalyze.append(au.UserAnalyze(user['_id'], user['fullName'], user['username'], user['counts']['Followers'], user['counts']['Following'], user['counts']['Media'], user['counts']['UserTags'], user['bio'], user['private'], user['media'], user['profilePicture']))

'''
for user in usersToAnalyze:
    print(user.userDetails())
'''
suspiciousUsers = []
for user in usersToAnalyze:
    user.analyze()
    if user.isSuspicious():
        suspiciousUsers.append(user)

