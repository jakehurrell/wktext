import requests
import json
import datetime

from config import wkKey

WKBASE = "https://api.wanikani.com/v2/"
WKHEADER = {"Authorization": "Bearer " + wkKey}

dt = str(datetime.datetime.utcnow().isoformat()) + "Z"

resp = requests.get(WKBASE + "summary", headers=WKHEADER)
subjectID = (resp.json())["data"]["reviews"][0]["subject_ids"][1]
nextreview = (resp.json())["data"]["reviews"][0]["available_at"]

print(nextreview)
print(subjectID)
resp = requests.get(WKBASE + "subjects/{}".format(subjectID), headers=WKHEADER)
print(resp.json()["data"]["characters"])

#"Content-Type": "application/json; charset=utf-8"

WKPOSTHEADER = {"Authorization": "Bearer " + wkKey, "Content-Type": "application/json; charset=utf-8", "WaniKani-Revision": "20170710"}

resp = requests.put(WKBASE + "study_materials/{}".format(subjectID), headers=WKPOSTHEADER, data={
    "study_material": {
        "meaning_note": "absolutely meaninglesssssssssssssssssssssss",
    }
})

print(resp)



# subject ID is a valid alternative to using assignment id
#found in "create a review"

exit()

# create a review means the review is finished and you are just communicating how many times the meaning/reading was incorrect

print(subjectID)

print(dt)

resp = requests.post(WKBASE + "reviews/", headers=WKHEADER, data={
    "review": {
        "assignment_id": subjectID,
        "incorrect_meaning_answers": 0,
        "incorrect_reading_answers": 0
    }
})

print(resp)
print(resp.json())

#resp = requests.get(WKBASE + "assignments/{}".format(data), headers=WKHEADER)
# print(resp.json())
