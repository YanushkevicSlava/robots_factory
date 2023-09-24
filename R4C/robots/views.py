from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Robot


class RobotAddView(CreateView):
    """
    Класс по созданию обьекта robot.
    """
    model = Robot
    fields = "serial", "model", "version", "created"
    success_url = reverse_lazy("robots:robots_list")


class RobotListView(ListView):
    """
    Класс получения списка существующих роботов.
    """
    queryset = Robot.objects.all()
