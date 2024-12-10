from django.shortcuts import render
from django.views.generic import ListView
from .models import Project

def ExampleListView(request):
    # Fetch all projects from the database
    projects = Project.objects.all()
    
    # Render the template with the projects context
    return render(request, 'previous_projects/examples.html', {'projects': projects})