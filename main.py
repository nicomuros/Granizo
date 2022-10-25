from radarUpdateChecker import *
from imgAnalyzer import *
from sms import *

url = "https://www2.contingencias.mendoza.gov.ar/radar/sur.gif"

#TESTING imgAnalyzer
imgName = "images/1918.gif"
clouds = []
clouds = imgAnalyzer(imgName)

'''
imgName = "lastImage.gif"
clouds = []
if newImage(url,imgName):
    clouds = imgAnalyzer(imgName)
    print(clouds)
'''
if clouds:
    
    sendWhatsapp("+542604338179","ALERTA: NUBE DE PIEDRA")
