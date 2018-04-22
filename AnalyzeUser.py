import google_image_search as gis
import imageSearchResult as isr

class UserAnalyze:
    'Analyze user account'
    
    
    def __init__(self, Id, fullName, userName, numOfFollowers, numOfFollowing, numOfMedia, numOfUserTags, bio, isPrivate, media, profilePic = None):
        #details
        self.Id = Id
        self.fullName = fullName
        self.userName = userName
        self.numOfFollowers = numOfFollowers
        self.numOfFollowing = numOfFollowing
        self.numOfMedia = numOfMedia
        self.numOfUserTags = numOfUserTags
        self.bio = bio
        #self.tags = tags
        #self.hashtags = hashtags
        self.isPrivate = isPrivate
        self.media = media
        #results
        self.postVSfollowers = None
        self.followingVSfollowers = None
        self.suspiciousName = 0
        self.emptyProfile = 0
        #self.reuseContent = None
        self.suspiciousHashtags = None
        self.profilePic = profilePic
        self.profilePicSR = isr.imageSearchResult()

    def userDetails(self):
        return "id=", self.Id, "name=", self.fullName, "username=", self.userName, "follow=", self.numOfFollowing, "following", self.numOfFollowers, "media=", self.numOfMedia, "isPrivate?=", self.isPrivate

    def calcRelations(self):
        self.postVSfollowers = self.numOfMedia/self.numOfFollowers
        self.followingVSfollowers = self.numOfFollowing/self.numOfFollowers

    def detectSuspiciousName(self):
        if self.fullName != False:
            nameTmp = self.fullName
            usernameTmp = self.userName
            usernameTmp.lower()
            nameTmp.lower()
            numOfFullName = 0
            numOfAppears = 0
            for word in nameTmp:
                numOfFullName += 1
            for word in nameTmp:
                if usernameTmp.find(word) != -1:
                    numOfAppears += 1
            self.suspiciousName = numOfAppears/numOfFullName
        else:
            self.suspiciousName = 0

    def emptyProfileScore(self):
        if self.profilePic != None:
            self.emptyProfile += 1
        else: 
            print('username:'+self.userName+' has no profile pic')
            print(self.profilePic)
        if self.bio != False:
            self.emptyProfile += 1
        if self.numOfFollowers != 0:
            self.emptyProfile += 1
        if self.numOfFollowing != 0:
            self.emptyProfile += 1
        if self.numOfMedia != 0:
            self.emptyProfile += 1
       
    def reuseContent(self):
        self.profilePicSR = gis.google_image_search(self.profilePic).ReverseImageLookup()
        
    def analyze(self):
        self.calcRelations()
        self.detectSuspiciousName()
        self.emptyProfileScore()
        self.reuseContent()
        
    def isSuspicious(self):
        if (self.profilePicSR.numbersOfLinks > 3 & self.profilePicSR.numbersOfPages > 2) | self.isPrivate :
            return True
        return False
        
        