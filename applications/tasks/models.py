from django.db import models
from applications.common.models import BaseMdoel
from django.contrib.auth import get_user_model


User = get_user_model()

class Task(BaseMdoel):

    priority_choices = [
        (1, 'Low'),
        (2, 'Important'),
        (3, 'Critical'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(verbose_name='Task Title', max_length=128)    
    description = models.TextField(verbose_name='Task Description', blank=True, null=True)
    priority = models.IntegerField(verbose_name='Task Priority' ,choices=priority_choices, default=1) 
    is_done = models.BooleanField(verbose_name='Task Status ( is done )',  default=False)

    def __str__(self) -> str:
        return f'{self.title}' 
    
