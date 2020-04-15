import fbchat
from fbchat import Client
import json
def account():
    try:
        with open('JSON_FILE\\data.json') as f:
            data1 = json.load(f)
            return data1
    except:
        return None

def message(name,msg):
    data1=account()
    username = data1['username']
    password = data1['password']
    client = fbchat.Client(username, password)
    client1 = Client(username, password)
    friends = client1.searchForUsers(name=name)
    friend = friends[0]
    sent = client.send(fbchat.Message(msg), friend.uid)
    if sent:
        return('message sent')

