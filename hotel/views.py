from django.shortcuts import render

from .models import Hotel
# Create your views here.

def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'home.html', {'hotels': hotels})