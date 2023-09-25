from django.db.models.signals import post_save
from django.dispatch import receiver
from robots.models import Robot
from .models import Order
from .services import send_email


@receiver(post_save, sender=Robot)
def check_new_robot_in_orders(sender, instance, created, **kwargs):
    """
    Функция сигнал, которая проверяет нового робота на предварительный заказ.
    Если заказ на этого робота существует, то отправляет письмо покупателю.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    """
    if created:
        orders = Order.objects.filter(robot_serial=instance.serial)
        if orders.exists():
            order = orders[0]
            customer = order.customer
            send_email(customer=customer, robot=instance)
