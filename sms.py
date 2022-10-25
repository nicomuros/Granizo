import http.client
from tokens import *
def sendWhatsapp(number,body):
    conn = http.client.HTTPSConnection("api.ultramsg.com")

    payload = "token=" + token + "&to=" + number + "&body=" + body + "&priority=1&referenceId="

    headers = { 'content-type': "application/x-www-form-urlencoded" }

    conn.request("POST", "/instance21246/messages/chat", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

sendWhatsapp("+542604338179" , "prueba token")