from django.shortcuts import render, get_object_or_404
from .models import Offer

# Create your views here.
def OfferListView(request):
    # Fetch all projects from the database
    offers = Offer.objects.filter(available=True)
    
    # Render the template with the projects context
    return render(request, 'pricing/offers_list.html', {'offers': offers})

def OfferDetailView(request, slug):
    offer = get_object_or_404(Offer, slug=slug)

    return render (request, 'pricing/offer_detail.html', {'offer' : offer})