from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

def home_view(request):
    return HttpResponse('<h1>Home Page<h1>')
def about_viwe(request):
    return HttpResponse('<h1>About Page<h1>')
def contact_viwe(request):
    return HttpResponse('<h1>Contact Page<h1>')

