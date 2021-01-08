import requests

def wkget(endpoint, wkKey):

    resp = requests.get(
        "https://api.wanikani.com/v2/" + endpoint,
        headers={"Authorization": "Bearer " + wkKey}
    )

    return resp