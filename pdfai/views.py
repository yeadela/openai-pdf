from django.shortcuts import render
from .chat import chatPDF
from .summarize import summarize
import store

# Create your views here.

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
    