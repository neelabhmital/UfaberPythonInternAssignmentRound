# Generated by Django 3.2.2 on 2021-05-07 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('name', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('duration', models.CharField(max_length=50)),
                ('task_created_at', models.DateTimeField(auto_now_add=True)),
                ('task_updated_at', models.DateTimeField(auto_now=True)),
                ('publish', models.DateField(default=django.utils.timezone.now)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'tasks',
                'ordering': ['task_created_at'],
            },
        ),
    ]
