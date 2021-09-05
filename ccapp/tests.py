from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import CurveCoffee

# Create your tests here.


class CoffeeBlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='user', password='password')
        test_user.save()

        test_post = CurveCoffee.objects.create(
            customer=test_user,
            drink='nescafe',
            description='hot drinks 3 in 1'
        )
        test_post.save()

    def test_blog_content(self):
        post = CurveCoffee.objects.get(id=1)
        actual_customer = str(post.customer)
        actual_drink = str(post.drink)
        actual_description = str(post.description)
        self.assertEqual(actual_customer, 'user')
        self.assertEqual(actual_drink, 'nescafe')
        self.assertEqual(actual_description, 'hot drinks 3 in 1')