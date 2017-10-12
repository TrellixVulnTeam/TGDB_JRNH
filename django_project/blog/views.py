from django.http import HttpResponse
import datetime
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello Django</h1>")

def today_is(request):
    now = datetime.datetime.now()
    return render_to_response('blog/datetime.html', {'now': now})
