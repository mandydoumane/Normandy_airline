from django.urls import path
from airline import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.vol_resa, name='vol_resa'),
]