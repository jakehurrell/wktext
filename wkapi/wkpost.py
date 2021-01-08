import requests

#EXAMPLE of data structure
#
#data = {
#    "study_material": {
#        "subject_id": subjectID,
#        "meaning_note": "insert meaning here",
#        "reading_note": "insert reading note here",
#    }}

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