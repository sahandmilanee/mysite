from django.urls import path
from website.views import *

urlpatterns = [
    path('index', home_view),
    path('about', about_viwe),
    path('contact', contact_viwe)
]