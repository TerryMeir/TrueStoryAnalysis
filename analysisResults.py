import imageSearchResult as isr
import AnalyzeUser as au

class analysisResults:
    'AnalyzeUser results'
    def __init__(self, user, isSuspicious):
        self.userID = user.Id
        self.isSuspicious = isSuspicious
        self.isBot = None
        self.postVSfollowers = user.postVSfollowers
        self.followingVSfollowers = user.followingVSfollowers
        self.suspiciousName = user.suspiciousName
        self.emptyProfile = user.emptyProfile
        self.googleSRnumOfLinks = user.profilePicSR.numbersOfLinks
        self.googleSRnumOfPages = user.profilePicSR.numbersOfPages
        self.numOfFollowers = user.numOfFollowers
        self.numOfFollowing = user.numOfFollowing
        self.numOfMedia = user.numOfMedia
        self.numOfUserTags = user.numOfUserTags
        self.isPrivate = user.isPrivate
'''    
    def __init__(self, isSuspicious, postVSfollowers, followingVSfollowers, suspiciousName, emptyProfile, profilePicSR):
        self.isSuspicious = isSuspicious
        self.isBot = None
        self.postVSfollowers = postVSfollowers
        self.followingVSfollowers = followingVSfollowers
        self.suspiciousName = suspiciousName
        self.emptyProfile = emptyProfile
        self.profilePicSR = profilePicSR
 '''
