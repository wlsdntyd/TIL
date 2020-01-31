from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('free/', views.free, name='free'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/qnvote/', views.qnvote, name='qnvote'),
]