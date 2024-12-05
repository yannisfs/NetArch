from . import views
from django.urls import path

app_name = "team"

urlpatterns = [
    path('', views.homepageview, name="homepage"),
]