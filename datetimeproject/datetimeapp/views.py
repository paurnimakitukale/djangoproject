from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def datetimeinfo(request):
    date = datetime.datetime.now()
    h =  int(date.strftime('%H'))
    msg='<h1>hello guest very'
    if h<12:
        msg+='Good morning'
    elif h<16:
         msg+='Good Afternoon'
    elif h<21:
        msg+='Good Evening' 
    else:
        msg+='Good Night' 
    msg+='</h1><hr>' 
    msg+='<h1>Hello Now the server time is:'+str(date)+'</h1>'             
    return HttpResponse(msg)