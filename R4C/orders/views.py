from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Order


class OrderCreateView(CreateView):
    model = Order
    fields = "customer", "robot_serial"
    success_url = reverse_lazy("orders:orders_list")


class OrderListView(ListView):
    queryset = Order.objects.select_related("customer").all()


