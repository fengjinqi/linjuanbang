from django.urls import path

from apps.jd_app import views
urlpatterns = [
    path('getList', views.getList),
    path('category', views.category),
    path('get_banner', views.get_banner),
]
