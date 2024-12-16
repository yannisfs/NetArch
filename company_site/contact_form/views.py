from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import Message
from pricing.models import Offer

# Create your views here.
def ContactFormView(request):
    offer_obj = None
    requested_quote = False

    if 'offer_slug' in request.GET:
        offer_slug = request.GET['offer_slug']
        offer_obj = get_object_or_404(Offer, slug=offer_slug)

    if 'requested_quote' in request.GET:
        requested_quote = True

    # Predefine a message if a quote is requested
    initial_data = {}
    if requested_quote and offer_obj:
        initial_data['content'] = f"I would like a quote for {offer_obj.title}. Please provide more details."

    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data['name'],
                surname=data['surname'],
                company=data['company'],
                email=data['email'],
                content=data['content'],
                offer=offer_obj,
                requested_quote=requested_quote
            )
        
    else:
        form = ContactForm(initial=initial_data)

    return render(request, 'contact_form/contact_form.html', {'form': form})