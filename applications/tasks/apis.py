from rest_framework import viewsets, serializers
from applications.tasks.models import Task


class TaskApi(viewsets.ModelViewSet):

    class TaskSerializer(serializers.ModelSerializer):

        class Meta:
            model = Task
            fields = '__all__'


    queryset = Task.objects.all()
    serializer_class = TaskSerializer
