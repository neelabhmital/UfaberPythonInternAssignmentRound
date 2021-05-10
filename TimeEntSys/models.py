from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from project.models import project
#model created here
class Task(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(project, related_name='project', null = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.CharField(max_length=50)
    task_created_at = models.DateTimeField(auto_now_add=True)
    task_updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def get_duration(self):
        return self.end_time - self.start_time
    def get_name(self):
        return self.name
    def get_starttime(self):
        return self.start_time
    def get_endtime(self):
        return self.end_time

    class Meta:
        db_table = 'tasks'
        ordering = [ 'task_created_at' ]
        verbose_name = 'task'
        verbose_name_plural = 'Tasks'

    @property
    def get_contentType(self):
        return ContentType.objects.get_for_model(self.__class__)

    def __str__(self):
        return "{}".format(self.name)