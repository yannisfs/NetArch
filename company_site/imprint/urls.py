from . import views
from django.urls import path

app_name = "imprint"

urlpatterns = [
    path('', views.ImprintView, name="imprint"),
]