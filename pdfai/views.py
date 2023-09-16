from django.shortcuts import render
from .chat import chatPDF
from .summarize import summarize
from . import store
from . import upload
from .llmRequest import parseLLMRequest
from .azureSearch import cognitiveSearch

# Create your views here.
def llmRequest(request):
    return parseLLMRequest(request)

def cognitiveSearch(request):
    return cognitiveSearch(request)

def chat(request):
    return chatPDF(request)

def summarize(request):
    return summarize(request)

def add_embedding(request):
    return store.add_embedding()

def get_all_embeddings(request):
    return store.get_all_embeddings()

def delete_embedding(request):
    return store.delete_embedding()

def upload(request):
    return upload.upload(request)
    