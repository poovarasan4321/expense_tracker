from django.core.management.base import BaseCommand
from tracker.models import Transaction

class Command(BaseCommand):
    help = 'Clear monthly data'

    def handle(self, *args, **kwargs):
        Transaction.objects.all().delete()
        self.stdout.write("Monthly data cleared")