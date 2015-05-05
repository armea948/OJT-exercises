from django.http import HttpResponse
import datetime

#from django.template import Context
#from django.template.loader import get_template
from django.shortcuts import render


def current_datetime(request):
    now = datetime.datetime.now()
    #template = get_template('current_datetime.html')
    #html = template.render(Context({'current_date': now}))
    #return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date': now},)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    context = {'hour_offset': offset, 'next_time': dt}
    return render(
        request,
        'hours_ahead.html',
        context,
    )

def hello(request, num=None):
    message = "Hello World"
    if num:
        message = "Hello World, the number is {}".format(num)
    return HttpResponse(message)

