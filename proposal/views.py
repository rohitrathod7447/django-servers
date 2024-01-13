from django.shortcuts import render
import os
from django.conf import settings

def ask(request):

    ask_name = 'asking bear.png'
    ask_path = os.path.join(settings.MEDIA_URL, 'images', ask_name)

    params = {'ask': ask_path}
    return render(request, 'ask.html', params)

def yes(request):
    return render(request, 'yes.html')