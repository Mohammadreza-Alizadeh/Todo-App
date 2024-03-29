# Generated by Django 4.1.6 on 2023-03-30 07:15

from django.db import migrations


def default_priority(apps, schema_editor):
    
    Priority = apps.get_model("home", "Priority")
    for priority in ['Important', 'Okay', 'WhoCares']:
        Priority.objects.create(priority=priority)
        





class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
         migrations.RunPython(default_priority),
    ]
