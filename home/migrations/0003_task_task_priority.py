# Generated by Django 4.1.6 on 2023-03-02 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_priority_alter_task_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_tasks', to='home.priority'),
        ),
    ]
