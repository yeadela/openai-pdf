from django.shortcuts import render
from .llmRequest import parseLLMRequest
from .azureSearch import cognitiveSearch
from .rules import test1, addRules,getRules,getRulesMappingById, editRules, getHandlers
from .uploadFile import uploadFiles1, uploadFiles
from .export import exports

# Create your views here.
def llmRequest(request):
    return parseLLMRequest(request)

def cognitiveSearch(request):
    return cognitiveSearch(request)

def addRule(request):
    return addRules(request)

def editRule(request):
    return editRules(request)

def getRule(request):
    return getRules(request)

def getRulesMapping(request):
    return getRulesMappingById(request)

def uploadFile(request):
    return uploadFiles1(request)

def getHandler(request):
    return getHandlers(request)

def export(request):
    return exports(request)

def test11(request):
    return test1(request)

