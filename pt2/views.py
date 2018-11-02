from django.shortcuts import render
from django.http import request
import pandas as pd


# Create your views here.
def index(rq_request:request):
    context = {}
    return render(rq_request,'index.html',context)