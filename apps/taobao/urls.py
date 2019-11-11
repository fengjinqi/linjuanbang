from django.urls import path
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('search', views.getSearch),
    path('banner', views.getTaoBanners),
    path('getCategory', views.getCategory),
    path('getHome', views.getHome),
    path('getTbkTpwd', views.getTbkTpwd),
]
