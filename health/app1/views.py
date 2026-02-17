from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reg(request):
    return render(request, 'reg.html')

