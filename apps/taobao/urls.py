from django.urls import path
from . import views
urlpatterns = [
    path('search', views.getSearch),
    path('banner', views.getTaoBanners),
    path('getCategory', views.getCategory),
    path('getHome', views.getHome),
]
