from django.urls import path, include 


urlpatterns = [
   path('jwt/', include('applications.authentication.urls')),
   path('todo/', include('applications.tasks.urls'))
]
