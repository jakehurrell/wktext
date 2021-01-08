import requests

#EXAMPLE of data structure
#
#data = {
#    "review" : {
#        "subject_id": ####,
#        "incorrect_meaning_answers": 0,
#        "incorrect_reading_answers": 0
#    }
#}

def wkpost(endpoint, wkKey, data):

    resp = requests.post(
        "https://api.wanikani.com/v2/" + endpoint,
        headers={
            "Authorization": "Bearer " + wkKey,
            "Content-Type": "application/json; charset=utf-8",
            "WaniKani-Revision": "20170710"
        },
        json=data
    )

    return resp