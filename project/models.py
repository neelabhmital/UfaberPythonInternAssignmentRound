from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

#model created here
class project(models.Model):
    proj_name = models.CharField(max_length=50)
    proj_is_active = models.BooleanField(default=True)
    proj_created_at = models.DateTimeField(auto_now_add=True)
    proj_updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'projects'
        ordering = [ 'proj_name' ]
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return "{}".format(self.proj_name)

    @property
    def get_tasks(self):
        return Task.objects.filter(projects__proj_name=self.proj_name)