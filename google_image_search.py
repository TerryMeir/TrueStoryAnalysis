import re
import urllib.request
from http.cookiejar import CookieJar
import imageSearchResult as isr

class google_image_search:
    
    def __init__(self, imageURL = None):
        self.cj = CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        self.opener.addheaders =  [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]
        self.imageURL = imageURL
        self.googlePath = 'https://www.google.com/searchbyimage?&image_url='+self.imageURL
        self.sourceCode = None
        self.numOfReusePic = 0
        self.numOfpageResults = 0

    def ReverseImageLookup(self):
        self.sourceCode = self.opener.open(self.googlePath).read()
        findLinks = re.findall(r'<img src', self.sourceCode.decode('utf-8'))
        self.numOfReusePic = len(findLinks)
        numbersOfPages = re.findall(r'<a aria-label="Page ', self.sourceCode.decode('utf-8'))
        self.numOfpageResults = len(numbersOfPages)+1
        return isr.imageSearchResult(self.imageURL, self.numOfReusePic, self.numOfpageResults)

    def PrintSourceCode(self):
        print(self.sourceCode)
        
'''       
    findLinks = re.findall(r'<img src', sourceCode.decode('utf-8'))
    for eachThing in findLinks:
        print(eachThing)
        
    numbersOfPages = re.findall(r'<a aria-label="Page ', sourceCode.decode('utf-8'))
    print(len(numbersOfPages)+1)
'''