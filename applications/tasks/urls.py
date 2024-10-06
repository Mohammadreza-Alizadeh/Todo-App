from django.urls import path , include
from rest_framework.routers import DefaultRouter
from applications.tasks.apis import TaskApi

router = DefaultRouter()
router.register('', TaskApi, basename='task')

urlpatterns = [
    path('', include(router.urls))
]