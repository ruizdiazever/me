from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    print(type(projects))
    return render(request, "portfolio/portfolio.html", {'projects':projects}) # Ultimo parametro es un diccionario
