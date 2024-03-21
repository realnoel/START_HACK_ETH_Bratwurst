# example/urls.py
from django.urls import path

from example.views import register, login, logout, recommender, fund_list


urlpatterns = [
    path('funds/', fund_list, name='fund_list'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('recommender/', recommender, name='recommender'),
]