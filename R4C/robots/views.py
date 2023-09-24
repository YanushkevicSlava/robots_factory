from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.http import HttpResponse, HttpRequest
from .models import Robot
from .services import create_data_to_excel


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


def week_exel_report(request: HttpRequest) -> HttpResponse:
    """
    Функция получения Excel отчёта.
    """
    data = create_data_to_excel()
    response = HttpResponse(data.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml"
                                                      ".sheet")
    response['Content-Disposition'] = 'attachment; filename=week_robots_report.xlsx'
    return response
