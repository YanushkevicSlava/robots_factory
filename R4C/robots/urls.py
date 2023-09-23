from django.urls import path
from .views import RobotAddView, RobotListView


app_name = 'robots'

urlpatterns = [
    path("add-robot/", RobotAddView.as_view(), name="robot_add"),
    path("robots-list/", RobotListView.as_view(), name="robots_list")
]