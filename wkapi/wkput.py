import requests

#EXAMPLE of data structure
#
#data = {
#    "study_material": {
#        "subject_id": subjectID,
#        "meaning_note": "updated meaning here",
#        "reading_note": "updated reading note here",
#    }}

def wkput(endpoint, wkKey, data):

    resp = requests.put(
        "https://api.wanikani.com/v2/" + endpoint,
        headers={
            "Authorization": "Bearer " + wkKey,
            "Content-Type": "application/json; charset=utf-8",
            "WaniKani-Revision": "20170710"
        },
        json=data
    )

    return resp