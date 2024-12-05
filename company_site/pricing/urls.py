from . import views
from django.urls import path

app_name = "pricing"

urlpatterns = [
    path('', views.homepageview, name="homepage"),
]