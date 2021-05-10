from django.contrib import admin
from .models import project

class projectAdmin(admin.ModelAdmin):

    list_display = [
                     "id",
                     "proj_name",
                     "timestamp",
                     "last_updated"
                   ]

    list_display_links = [
                            "proj_name",
                            "timestamp",
                            "last_updated"
                         ]

    list_filter = [
                    "proj_name",
                    "timestamp",
                    "last_updated"
                  ]

    ordering = [ "timestamp" ]

admin.site.register(project, projectAdmin)