from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='TokenObtainPairView'),
    path('refresh/', TokenRefreshView.as_view(), name='TTokenRefreshView'),
    path('verify/', TokenVerifyView.as_view(), name='TokenVerifyView'),
]
