from django.core.management import BaseCommand
from customers.models import Customer


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Create customer")

        customer = Customer.objects.get_or_create(
            email="bob@gmail.com"
        )
        self.stdout.write(f"Created customer {customer}")
