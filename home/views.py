from django.shortcuts import render
from django.http import HttpResponse
from . import example

# Create your views here.
def index(request):
    r = example.get_request()
    response = f"{r}\n{r.text}"
    return HttpResponse(response)