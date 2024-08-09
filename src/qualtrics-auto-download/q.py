#qualtrics api doccumentation: https://api.qualtrics.com/
# https://api.qualtrics.com/5d17de1a27084-example-use-cases-walkthrough
# https://api.qualtrics.com/5e86e383167d5-getting-survey-responses-via-the-new-export-ap-is

import requests
#import zipfile
#import io
import os

from dotenv import load_dotenv, dotenv_values
load_dotenv()

dir_save_survey = os.getenv("dir_save_survey")
survey_id = os.getenv("survey_id")

path = os.getenv("survey_id")

#User Parameters
api_token: str = os.getenv("api_token")
file_format = "csv"
data_center = os.getenv("data_center")

#Static Parameters
request_check_progress = 0.0
progress_status = "in progress"
base_url = "https://{0}.qualtrics.com/API/v3/surveys/{1}/export-responses/".format(data_center, survey_id)
headers = {
    "content-type": "application/json",
    "x-api-token": api_token,
}

# Step 1: Creating Data Export
downloadRequestUrl = base_url
downloadRequestPayload = '{"format":"' + file_format + '"}'
downloadRequestResponse = requests.request("POST", downloadRequestUrl, data=downloadRequestPayload, headers=headers)
progressId = downloadRequestResponse.json()["result"]["progressId"]
print(downloadRequestResponse.text)