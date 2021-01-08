import requests
from twilio.rest import Client

resp = requests.get(
    "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(twilAccSID),
    auth= HTTPBasicAuth(twilAccSID, twilAuthTok)
)
print(resp)
print(resp.json())

exit()

twilClient = Client(twilAccSID, twilAuthTok)

#message = twilClient.messages.create(
#    body="Test from wktext",
#    from_="+16472501247",
#    to="+16479904096"
#)