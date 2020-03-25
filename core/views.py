from django.shortcuts import render

# Create your views here.
# Crear 4 funciones home, about, portfolio & contact

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")