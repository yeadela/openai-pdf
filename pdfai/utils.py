import json

def getReqParamValue(request,param):
    if request.method == 'GET':
        return request.GET.get(param)
    else:
        return json.loads(request.body).get(param)