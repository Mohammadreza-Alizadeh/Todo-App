from rest_framework import viewsets, serializers
from applications.tasks.models import Task
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskApi(viewsets.ModelViewSet):

    class TaskSerializer(serializers.ModelSerializer):

        class Meta:
            model = Task
            fields = '__all__'


    serializer_class = TaskSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
 
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
