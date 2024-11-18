from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("service/", views.ServiceDetails.as_view(), name="service-details"),
    path("starter/", views.StarterPage.as_view(), name="starter-page"),
]
