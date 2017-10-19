from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.conf import settings
import datetime

def index(request):
    return HttpResponse("<h1>Hello Django</h1>")

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {
                                    'now': now,
                                    'template': 'blog/nav.html',
                                    'base_dir': settings.BASE_DIR
                                    })
