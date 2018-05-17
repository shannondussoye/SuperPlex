import requests
import time
import datetime
from config import vultr_api_key
headers={"API-Key": vultr_api_key}

print(datetime.datetime.now())
def serverstatus():
    serverdetails = (requests.get("https://api.vultr.com/v1/server/list", headers=headers)).json()
    return serverdetails

serverdetails=serverstatus()
serverid = list(serverdetails.keys())[0]
serverstate=serverdetails[serverid]["server_state"]

while serverstate!="ok":
    time.sleep(300)
    serverstate = serverstatus()
    if(serverstate=="ok"):
        requests.post("https://api.vultr.com/v1/server/destroy", headers=headers, data=serverid)
        print("Server Destroyed")
        break
print(datetime.datetime.now())