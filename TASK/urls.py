from django.urls import path
from TASK.views import TaskView

urlpatterns = [
    path('task/',TaskView.as_view()),
     
]