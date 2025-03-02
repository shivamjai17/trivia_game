from django.urls import path
from game.views import get_random_clues, check_answer,get_csrf_token,home

urlpatterns = [
    path('api/get-random-clues/', get_random_clues, name="get_random_clues"),
    path('api/check-answer/', check_answer, name="check_answer"),
    path("api/get-csrf-token/", get_csrf_token, name="get_csrf_token"),
    path('',home,name='name') 
]
