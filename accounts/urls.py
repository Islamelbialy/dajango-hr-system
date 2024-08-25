from django.urls import path
from . import views
from hrsystem import settings 

urlpatterns = [
    path('signup/', views.signUp ,name="signUp"),
    path('logout/', views.logout ,name="logout"),
    path('login/', views.login ,name="login"),
    path('changePassword/', views.changePassword ,name="changePassword"),
]
