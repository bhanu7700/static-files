from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    MY_DICT = {"insert_me":"Hello i am from views.py"}
    return render(request, 'index.html', context = MY_DICT)
