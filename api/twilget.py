import requests
from requests.auth import HTTPBasicAuth

def twilget(sender, receiver, twilAccSID, twilAuthTok):

    resp = requests.get(
        "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(twilAccSID),
        params=(("To", receiver), ("From", sender)),
        auth= HTTPBasicAuth(twilAccSID, twilAuthTok)
    )

    return resp.json()["messages"][0]["body"]
