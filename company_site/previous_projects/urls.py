from . import views
from django.urls import path

app_name = "previous_projects"

urlpatterns = [
    path('', views.homepageview, name="homepage"),
]