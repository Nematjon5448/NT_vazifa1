from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def add_to_session(request):
    request.session['name'] = "Nematjon"
    return HttpResponse("Salom")

def get_value_from_session(request):
    value = request.session.get('name')
    return HttpResponse(value)

def update_value_from_session(request):
    request.session['name'] = "Sardor"
    return HttpResponse("Updated")

def delete_value_from_session(request):
    del request.session['name']
    return HttpResponse("O'chirildi!!!")