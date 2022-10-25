from requests import get
import hashlib
from urllib.request import urlopen, Request

def checkUpdates(urlReceived):
    try:
        f = open('hash.txt','r')
    except:
        f = open('hash.txt','w')
        f.write("nohash")
        f.close()
        f = open('hash.txt','r')

    lastHash = f.read()
    
    f.close()
    url = Request(urlReceived,
            headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()
    currentHash = hashlib.sha224(response).hexdigest()
    if (lastHash != currentHash):
        f = open('hash.txt','w')
        f.write(currentHash)
        f.close        
        return True
    else: 
        return False

def downloadImage(url, imgName):
    with open(imgName, "wb") as file: 
            # get request
            response = get(url)
            # write to file
            file.write(response.content)

def newImage(url, imgName):
    if (checkUpdates(url)):
        downloadImage(url, imgName)
        return True
    else:
        return False


        
