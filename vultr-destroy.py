from config import vultr_api_key
import requests

headers = {"API-Key": vultr_api_key}
BaseUrl = "https://api.vultr.com/v1/"
data = ""


def vultrcall(string):
    url = BaseUrl + string
    return (requests.get(url, headers=headers, data=data)).json()


# def checkSnapshot():
#     SnapshotList=vultrCall("snapshot/list")
#     id = list(SnapshotList.keys())[0]
#     if (len(id)) > 0:
#         return SnapshotList[id]

def serverdetails():
    return vultrcall("server/list")

# list Server
ServerId = list(serverdetails().keys())[0]
data = {'SUBID': ServerId}


def vultrpost(path, pdata):
    url = BaseUrl + path
    p = requests.post(url, headers=headers, data=pdata)
    return ("Response: {}".format(p.text))

snapshot = vultrpost("snapshot/create", data)
print(snapshot)
#destroy=vultrpost("server/destroy",data)