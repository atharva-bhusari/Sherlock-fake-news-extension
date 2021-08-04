from django.shortcuts import render

# Create your views here.
import json
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .urlextract import prediction

def index(request):
    return HttpResponse("Hello, Your are at sherlock")

def predict_news(request):
    news_url = request.GET.get('news_url')
    print('news_url: ', news_url)

    data = {
        'prediction': prediction(news_url),
        'raw': 'Successful',
    }

    print('Data to be sent: ', data)
    return JsonResponse(data)
