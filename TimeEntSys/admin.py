from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = [
                     "id",
                     "name",

                     "start_time",
                     "end_time",
                     "duration",
                     "timestamp",
                     "last_updated"
                   ]

    list_display_links = [
                            "name",
                            "start_time",
                            "end_time",
                            "duration",
                            "timestamp",
                            "last_updated"    
                         ]

    list_filter = [
                    "name",
                    "timestamp",
                    "last_updated"
                  ]

    ordering = ["timestamp"]

admin.site.register(Task, TaskAdmin)