import requests
import json
import datetime

import wkapi
from config import wkKey

#dt = str(datetime.datetime.utcnow().isoformat()) + "Z"

resp = wkapi.wkget("summary", wkKey)
subjectID = (resp.json())["data"]["reviews"][0]["subject_ids"][0]
print(subjectID)
nextreview = (resp.json())["data"]["reviews"][0]["available_at"]
print(nextreview)

resp = wkapi.wkget("subjects/{}".format(subjectID), wkKey)
print(resp.json()["data"]["characters"])


data = {
    "study_material": {
        "meaning_note": "trying put",
        "reading_note": "this might work!",
    }}

resp = wkapi.wkput("study_materials/6651223", wkKey, data)
print(resp)
print(resp.json())

exit()



# subject ID is a valid alternative to using assignment id
#found in "create a review"

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
