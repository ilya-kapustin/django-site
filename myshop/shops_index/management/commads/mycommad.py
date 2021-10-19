from django.core.management.base import BaseCommand
from ...models import ShopsGroup, Shops


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(30):
            ShopsGroup.objects.create(name='ergferg', img='img', description='description')
        for i in range(500):
            Shops.objects.create(title='ergferg', code_thing='0', img='img', description='description',
                                 created_at='18.10.2021', updated_at='18.10.2021', finish_at='18.10.2021',
                                 price='10522', group_id=1, views_count='0', status='d')
