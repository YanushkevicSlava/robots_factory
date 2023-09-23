from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Robot


class RobotAddView(CreateView):
    model = Robot
    fields = "serial", "model", "version", "created"
    success_url = reverse_lazy("robots:robots_list")


class RobotListView(ListView):
    queryset = Robot.objects.all()
