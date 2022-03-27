from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    previousEvents = PreviousEvent.objects.all()
    return render(request, 'placeholder_home.html', {'previousEvents': previousEvents})
