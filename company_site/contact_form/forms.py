from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"*"})
    )
    surname = forms.CharField(
        label='Surname',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"*"})
    )
    company= forms.CharField(
        label='Company',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"* name@example.com"})
    )
    content = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder':"*"})
    )