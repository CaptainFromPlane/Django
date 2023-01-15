from django.shortcuts import render
from django.http import HttpResponse

def index2(request):
    output = render(request, 'hello2app/web.html')
    return   HttpResponse(output)  
