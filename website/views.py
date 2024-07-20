from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

def home_view(request):
    return render(request, 'website/index.html')
def about_viwe(request):
    return render(request,'website/about.html')
def contact_viwe(request):
    return render(request,'website/contact.html')

