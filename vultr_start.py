#Import API-Key
from config import vultr_api_key
from config import config
headers={"API-Key": vultr_api_key}

import requests
import pandas as pd
from pandas.io.json import json_normalize
import pyrebase

BaseUrl="https://api.vultr.com/v1/"

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#Define function to make api calls
def vultrCall(string):
    url=BaseUrl+string
    return (requests.get(url, headers=headers)).json()

def checkSnapshot():
    SnapshotList=vultrCall("snapshot/list")
    id = list(SnapshotList.keys())[0]
    if (len(id)) > 0:
        return(SnapshotList[id])
    else:
        print("No Snapshot found")
        exit(1)

SnapshotDetails=checkSnapshot()
if len(SnapshotDetails)>0:
    SnapshotId=SnapshotDetails["SNAPSHOTID"]

data = {'DCID': '19', 'VPSPLANID': '203', 'OSID': '164', 'SNAPSHOTID': SnapshotId}

#create Server from Snapshot
def createInstance():
    p = requests.post("https://api.vultr.com/v1/server/create", headers=headers, data=data)
    return("Response: {}".format(p.text))

ServerList=vultrCall("server/list")
#check if there is an instance running if not create from snapshot
if len(ServerList)==0:
    print("No Instance Running. Creating Instance...")
    # Create Instance with Snapshot
    #createInstance()