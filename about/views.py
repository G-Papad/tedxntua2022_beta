from django.shortcuts import render

# Create your views here.

def hello2(request):
    return render(request, 'placeholder_about.html', {})
