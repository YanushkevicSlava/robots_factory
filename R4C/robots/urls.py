from django.urls import path
from .views import RobotAddView, RobotListView, week_exel_report


app_name = 'robots'

urlpatterns = [
    path("add-robot/", RobotAddView.as_view(), name="robot_add"),
    path("robots-list/", RobotListView.as_view(), name="robots_list"),
    path("week-report", week_exel_report),
]
