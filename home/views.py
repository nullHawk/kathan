from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import kathan_integrator as integrator
import json
from django.http import JsonResponse
import requests
from django.urls import reverse

languages = {1:"Tamil", 2:"Telugu", 3:"Hindi", 4:"Malayalam", 5:"Marathi", 6:"Bengali", 7:"Assamese", 8:"Gujarati", 9:"Kannada", 10:"Oriya", 11:"Punjabi"}

# Create your views here.
def index(request):
    if request.method == 'POST':

        content = request.POST.get('content')
        source_language = int(request.POST.get('source_language'))
        target_language = int(request.POST.get('target_language'))

        endpoint = request.build_absolute_uri(reverse('translate'))
        body={
            "content": content,
            "source_language": source_language,
            "target_language": target_language
        }
        r = requests.post(endpoint, data=body)
        js = json.loads(r.text)

        response = {
            "languages" : languages,
            "content" : content,
            "translated_content" : js['translated_content'],
            "source_language": source_language,
            "target_language": target_language
        }
        request.session.update(response)
        return redirect(request.path)
    
    response = {
            "languages" : languages,
            "content" : request.session.get('content'),
            "translated_content" : request.session.get('translated_content'),
            "source_language": request.session.get('source_language'),
            "target_language": request.session.get('target_language')
        }
    return render(request, 'home/index.html', response)

@csrf_exempt
def translate(request):

    post_data = request.POST

    source_language = resolve_lang_code(int(request.POST.get('source_language')) if('source_language' in request.POST) else 0)
    content = request.POST.get('content')
    target_language = resolve_lang_code(int(request.POST.get('target_language')) if('target_language' in request.POST) else 0)

    # source_language = resolve_lang_code(3)
    # content = "मेरा नाम विहिर है और मैं भाषाावर्ष यूज कर रहा हूँ"
    # target_language = resolve_lang_code(1)


 

    if source_language == -1 or target_language == -1:
        response ={
        "status_code": "error", #we will return error code
        "message": "Invalid Language Code",
        "translated_content": None,
        }
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    else:
        integrator.initialize(source=source_language, target=target_language)
        r = integrator.get_request()

        js = json.loads(r.text)
        if "pipelineResponseConfig" not in js:
            response ={
                "status_code": "error", #we will return error code
                "message": "invalid input or language code",
                "translated_content": None,
            }
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        else:
            serviceID = js["pipelineResponseConfig"][0]['config'][0]["serviceId"]
            #modelId = js["pipelineResponseConfig"][0]['config'][0]["modelId"]
            api_endPoint_callbackUrl = js['pipelineInferenceAPIEndPoint']['callbackUrl']
            api_endpoint_key = js['pipelineInferenceAPIEndPoint']['inferenceApiKey']["name"]
            api_endpoint_value = js['pipelineInferenceAPIEndPoint']['inferenceApiKey']["value"]
            output = integrator.translate(
                api_endPoint_callbackUrl,
                api_endpoint_key,
                api_endpoint_value,
                source_language,
                target_language,
                serviceID,
                content)
            
            output_js = json.loads(output.text)
            if "pipelineResponse" not in output_js:
                response ={
                    "status_code": str(output), #we will return error code
                    "message": output.text,
                    "translated_content": None,
                }
                return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
            else:
                translated_content= output_js["pipelineResponse"][0]["output"][0]["target"]
                
                response = {
                    "status_code": str(output),
                    "message": "working",
                    "translated_content": str(translated_content)
                }

                return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
            


    


def resolve_lang_code(int_lang_code):
    str_lang_code = ""
    if int_lang_code == 1:
        return 'ta'
    if int_lang_code == 2:
        return 'te'
    if int_lang_code == 3:
        return 'hi'
    if int_lang_code == 4:
        return 'ml'
    if int_lang_code == 5:
        return 'mr'
    if int_lang_code == 6:
        return 'bn'
    if int_lang_code == 7:
        return 'as'
    if int_lang_code == 8:
        return 'gu'
    if int_lang_code == 9:
        return 'kn'
    if int_lang_code == 10:
        return 'or'
    if int_lang_code == 11:
        return 'pa'
    return -1