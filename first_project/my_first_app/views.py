from django.shortcuts import render
from django.http import HttpResponse
from my_first_app.models import Topic,WebPage,AccessRecord
# Create your views here.

def index_main(request):
    return HttpResponse("Hello World")

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # dict = {'insert_me':"Hello, I am now fist_app/index.html views.py"}
    return render(request, "first_app/index.html", context = date_dict)
