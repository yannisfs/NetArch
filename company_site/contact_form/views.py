from django.shortcuts import render
from .forms import ContactForm
from .models import Message

# Create your views here.
def ContactFormView(request):
    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data['name'],
                surname=data['surname'],
                company=data['company'],
                email=data['email'],
                content=data['content'] 
            )
        
    else:
        form = ContactForm()

    return render(request, 'contact_form/contact_form.html', {'form': form})