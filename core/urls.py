from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("service/", views.ServiceDetails.as_view(), name="service-details"),
    path("portfolio/", views.StarterPage.as_view(), name="portfolio-details"),
    path("starter/", views.StarterPage.as_view(), name="starter-page"),
    path("blog/", views.Blog.as_view(), name="blog"),
    path("blog-details/", views.BlogDetails.as_view(), name="blog-details"),
]
