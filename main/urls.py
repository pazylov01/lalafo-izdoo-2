from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('lk/', views.lk, name='lk'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('productadd/', views.productAdd, name='productadd'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),





]