from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model


class SnackTestCase(TestCase):
    def setUp(self):
        purchaser = get_user_model().objects.create(username="tester",password="tester")
        Snack.objects.create(
            name='Cookies',
            purchaser=purchaser,
            description='chocolate flavour'
        )

    def test_list_page_status_code(self):
        url = reverse('Snack_List')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('Snack_List')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')
