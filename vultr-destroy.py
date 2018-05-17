from config import vultr_api_key
import requests

headers = {"API-Key": vultr_api_key}
BaseUrl = "https://api.vultr.com/v1/"

def vultrcall(string):
    url = BaseUrl + string
    return (requests.get(url, headers=headers)).json()


# def checkSnapshot():
#     SnapshotList=vultrCall("snapshot/list")
#     id = list(SnapshotList.keys())[0]
#     if (len(id)) > 0:
#         return SnapshotList[id]

def serverdetails():
    return vultrcall("server/list")

# list Server
serverDetails=serverdetails()
ServerId = list(serverDetails.keys())[0]
data = {'SUBID': ServerId}


def vultrpost(path, pdata):
    url = BaseUrl + path
    return requests.post(url, headers=headers, data=pdata)

snapshot = vultrpost("snapshot/create", data)

if snapshot.status_code==200:
    print(snapshot.text)
    #print("Snapshot being created")
else:
    exit(1)




#print(snapshot.text)
#exit(1)


#destroy=vultrpost("server/destroy",data)