from django.shortcuts import render
from .models import Entity

# Create your views here.
def TeamView(request):
    entities = Entity.objects.all()
    return render(request, 'team/team.html', {'entities': entities})