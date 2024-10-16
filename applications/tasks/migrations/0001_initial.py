# Generated by Django 5.1.1 on 2024-10-06 02:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, verbose_name='Task Title')),
                ('description', models.CharField(blank=True, max_length=128, null=True, verbose_name='Task Description')),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Important'), (3, 'Critical')], default=1, verbose_name='Task Priority')),
                ('is_done', models.BooleanField(default=False, verbose_name='Task Status ( is done )')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
