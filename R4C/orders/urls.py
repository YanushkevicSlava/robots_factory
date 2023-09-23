from django.urls import path
from .views import OrderCreateView, OrderListView


app_name = 'orders'

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="order_create"),
    path("orders-list/", OrderListView.as_view(), name="orders_list")
]
