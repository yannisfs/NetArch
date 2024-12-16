from . import views
from django.urls import path

app_name = "contact_form"

urlpatterns = [
    path('', views.ContactFormView, name="contact"),
]