from django.http import HttpResponse
import datetime
from django import template

def index(request):
    return HttpResponse("<h1>Hello Django</h1>")

def today_is(request):
    now = datetime.datetime.now()
    t = template.Template("<html><body>Current date and time {{ now }}</body></html>")
    c = template.Context({'now': now})
    html = t.render(c)
    return HttpResponse(html)