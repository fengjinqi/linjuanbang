from django.urls import path
from . import views
urlpatterns = [
    path('', views.getTaoHome),
    path('banner', views.getTaoBanners),
    path('getCategory', views.getCategory),
    path('getHome', views.getHome),
]
