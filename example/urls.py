# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('recommender/', views.recommender, name='recommender'),
]