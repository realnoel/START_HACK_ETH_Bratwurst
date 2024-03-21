# example/urls.py
from django.urls import path

from example.views import register, login, logout, recommender, questionnaire


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('recommender/', recommender, name='recommender'),
    path('questionnaire/', questionnaire, name='questionnaire'),
]