from django.shortcuts import render

# Create your views here.
# src/pages/views.py
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Hello, World od Django!")