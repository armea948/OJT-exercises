from django.shortcuts import render
#from django.http import HttpResponse
from polls.models import Poll

def index(request):
    datas = Poll.objects.all()
    #html = ""
    #for data in datas:
    #    html += "<p>{}<p>".format((data.question))
    #return HttpResponse(html)
    return render(request, 'poll_temp.html', {'data': datas},)
