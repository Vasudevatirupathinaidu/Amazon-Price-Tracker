from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("delete-link/<str:pk>/", views.deleteLink, name="delete-link"),
    path("update-prices/", views.updatePrices, name="update-prices"),
]