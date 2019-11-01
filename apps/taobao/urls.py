from django.urls import path
from . import views
from apps.jd_app.views import getRush
urlpatterns = [
    path('search', views.getSearch),
    path('banner', views.getTaoBanners),
    path('getCategory', views.getCategory),
    path('getHome', views.getHome),
    path('getRush', getRush),
]
