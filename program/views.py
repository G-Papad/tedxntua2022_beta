from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request, 'placeholder_program.html', {})
