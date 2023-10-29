import requests
from . import auth

userID = auth.userID
ulcaApiKey = auth.ulcaApiKey
pipelineId = auth.pipelineId

source_lang = ""
target_lang = ""

endpoint = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"

header= {
    'userID' : userID,
    "ulcaApiKey" : ulcaApiKey
}



pipeline_config = {
    "pipelineTasks": [
        
        {
            "taskType": "translation",
            "config": {
                "language": {
                    "sourceLanguage": source_lang
                }
            }
        }
    ],
    "pipelineRequestConfig" : {
        "pipelineId" : pipelineId
    }
}

def initialize(source, target):
    global source_lang, target_lang, pipeline_config
    source_lang = source
    target_lang = target
    pipeline_config = {
        "pipelineTasks": [
            {
                "taskType": "translation",
                "config": {
                    "language": {
                        "sourceLanguage": source_lang,
                        "targetLanguage": target_lang
                    }
                }
            }
        ],
        "pipelineRequestConfig" : {
            "pipelineId" : pipelineId
        }
    }

def translate(api_endpoint, key, value, source, target, serviceID, content):

    header = {
        key : value,
    }
    body = {
        "pipelineTasks": [
            {
                "taskType": "translation",
                "config": {
                    "language": {
                        "sourceLanguage": source,
                        "targetLanguage": target
                    },
                    "serviceId": serviceID
                }
            }
        ],
        "inputData": {
            "input": [
                {
                    "source": content
                }
            ]
        }
    }
    r = requests.post(api_endpoint, headers=header, json=body)
    return r

def get_tts_content(target_lang, source_lang, content):

    return 
def get_request():
    r = requests.post(endpoint, headers=header, json=pipeline_config)
    return r



