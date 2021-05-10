from django.urls import path
from .views import *

app_name = "TimeEntSys"
urlpatterns = [
                path("<int:inp_id>/edit/", task_edit, name='edit'),
                path("<int:inp_id>/delete/", task_delete, name='delete'),
                path("<int:inp_id>/", taskDetails, name='Details'),
                path("new/", task_new, name='new'),
                path("all/", task_all, name='all')
              ]