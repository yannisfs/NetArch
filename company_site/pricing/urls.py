from . import views
from django.urls import path

app_name = "pricing"

urlpatterns = [
    path('', views.OfferListView, name="offers_list"),
    path('<slug:slug>/', views.OfferDetailView, name='offer_detail'),
]