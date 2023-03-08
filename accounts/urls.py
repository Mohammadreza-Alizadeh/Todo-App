from django.urls import path

from . import views


urlpatterns = [
     path('login/', views.login_user, name="login_user"),
     path('logout/', views.logout_user, name="logout_user"),
     path('signup/', views.user_signup, name="user_signup"),
]
