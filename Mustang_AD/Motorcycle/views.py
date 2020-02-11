from django.shortcuts import render

# Create your views here.


def Motorcycle(request):
    return render(request, 'Motorcycle.html')