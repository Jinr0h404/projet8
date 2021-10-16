from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'initialize database'

    def handle(self, *args, **kwargs):
        pass