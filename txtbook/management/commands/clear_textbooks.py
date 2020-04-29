from django.core.management.base import BaseCommand
from txtbook.models import Textbook


class Command(BaseCommand):
    def handle(self, *args,**options):
        Textbook.objects.all().delete()
