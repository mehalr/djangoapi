from django.http import HttpResponse
import json
from djangoapi.machineLearningModel import prediction


def sampleApiTest(request):
    context = {}
    if request.method == 'GET':
        context['requestType'] = 'GET'
        context['message'] = 'Application Received GET Request'
        context['data'] = 'Chhalaang!'
        return HttpResponse(json.dumps(context), content_type='application/json')
    requestData = json.loads(request.body)
    if requestData:
        context['requestType'] = 'POST'
        context['message'] = 'Application Received POST Request'
        context['dataReceived'] = requestData
        context['data'] = f"The requestType received was {requestData.get('requestType')} and message was {requestData.get('requestMessage')}"
    return HttpResponse(json.dumps(context), content_type='application/json')

def mlView(request):
    context = {}
    if request.method== "POST":
        requestData = json.loads(request.body)
        result = prediction(requestData)
        context['result'] = result
        return HttpResponse(json.dumps(context),content_type='application/json')

    return HttpResponse(json.dumps(context),content_type='application/json')
