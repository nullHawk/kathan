import requests
import auth

userID = auth.userID
ulcaApiKey = auth.ulcaApiKey
pipelineId = auth.pipelineId

endpoint = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"

header= {
    'userID' : userID,
    "ulcaApiKey" : ulcaApiKey
}

body = {
    "pipelineTasks": [
        {
            "taskType": "translation",
            "config": {
                "language": {
                    "sourceLanguage": "eng",
                    "targetLanguage": "hin"
                }
            }
        },
    ],
    "pipelineRequestConfig" : {
        "pipelineId" : pipelineId
    }
}

r = requests.post(endpoint, headers=header, json=body)

print(r)
print(r.text)
