from django.shortcuts import render

# Create your views here.
def ImprintView(request):
    return render(request, 'imprint/imprint.html')