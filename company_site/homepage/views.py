from django.shortcuts import render
from .models import Update

# Create your views here.
def HomepageView(request):
    updates = Update.objects.all()

    return render(request, 'homepage/home.html', {'updates': updates})
