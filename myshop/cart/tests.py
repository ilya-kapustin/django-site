from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from shops_index.models import Shops, Tag, ShopsGroup, ShopContacts, ShopsComm

User = get_user_model()


class CartTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        group = ShopsGroup.objects.create(
            name='Группа 1',
            img='images/no-image.jpg',
            description='Описание группы',
        )
        shop = Shops.objects.create(
            title='Названи товара',
            img='images/no-image.jpg',
            description='Описание товара',
            group=group,
        )
        user = User.objects.create_user(
            username="tester",
            password="12345",
        )

    def test_one(self):
        self.client.login(
            username="tester",
            password="12345",
        )
        shop = Shops.objects.first()
        url = f'/cart/add/{shop.id}/'
        data = {'quantity': 1, 'update': False}
        response = self.client.post(url, data)
        self.assertEqual(
            len(self.client.session[settings.CART_SESSION_ID]),
            1
        )
