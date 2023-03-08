from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('remove/<int:task_id>/', views.remove_task, name="remove_task" ),
    path('add/', views.add_task, name="add_task" ),
    path('change_priority/<int:task_id>/', views.change_priority, name="change_priority"),
    path('update/<int:task_id>', views.update_task, name="update_task")
]
