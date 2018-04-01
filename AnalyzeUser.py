# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:08:56 2018

@author: Terry
"""

class UserAnalyze:
    'Analyze user account'
    
    def __init__(self, Id, fullName, userName, numOfFollowers, numOfFollowing, numOfMedia, numOfUserTags, bio, isPrivate, media):
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
        #init results
        self.postVSfollowers = None
        self.followingVSfollowers = None
        self.suspiciousName = 0
        self.emptyProfile = None
        self.reuseContent = None
        self.suspiciousHashtags = None

    def printUserDet(self):
        return "id=", self.Id, "name=", self.fullName, "username=", self.userName, "follow=", self.numOfFollowing, "following", self.numOfFollowers, "media=", self.numOfMedia, "isPrivate?=", self.isPrivate

    def calcRelations(self):
        self.postVSfollowers = self.numOfMedia/self.numOfFollowers
        self.followingVSfollowers = self.numOfFollowing/self.numOfFollowers

    def detectSuspiciousName(self):
        nameTmp = self.fullName
        nameTmp.lower()
        for word in nameTmp:
            if self.userName.find(word) != -1:
                self.suspiciousName += 1


