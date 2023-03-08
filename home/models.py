from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Priority(models.Model):
    priority = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} : {self.priority}"



class Task(models.Model):

    task_name = models.CharField(max_length=64)
    task_description = models.TextField()
    task_date = models.DateTimeField(auto_now_add=True)
    task_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_tasks")
    task_status = models.BooleanField(default=False)
    task_priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null = True ,related_name="sub_tasks")

    def __str__(self):
        return f"{self.task_name} → {self.task_status}"
    

    