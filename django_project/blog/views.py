from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("<h1>Hello Django</h1>")

def today_is(request):
    now = datetime.datetime.now()
    html = "<html><body>Current date and time: {0}</body></html>".format(now)
    return HttpResponse(html)