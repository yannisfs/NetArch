from django.shortcuts import render
from .models import Offer

# Create your views here.
def OfferListView(request):
    # Fetch all projects from the database
    offers = Offer.objects.filter(available=True)
    
    # Render the template with the projects context
    return render(request, 'pricing/offers.html', {'offers': offers})