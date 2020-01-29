from django.urls import path
from . import views # . 현재 경로

urlpatterns = [
    path('main/', views.main, name='main'),
    path('shop/', views.shop, name='shop'),
    # path('article/', views.article, name='article'),
]
