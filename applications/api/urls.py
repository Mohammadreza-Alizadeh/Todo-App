from django.urls import path, include 


urlpatterns = [
   path('jwt/', include('applications.authentication.urls')),
]
