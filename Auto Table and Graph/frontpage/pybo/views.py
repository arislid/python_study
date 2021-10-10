#-*- coding: utf-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    
    return HttpResponse("PYBO에 오신 것을 환영합니다!!")
    # Korean character data is broken!! 
    # This will be the problem when decoding and encoding between UTF-8 and EUC-kr