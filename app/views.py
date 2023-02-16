from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def redirected(request):
    print(request.__dict__)
    return HttpResponse("done")
