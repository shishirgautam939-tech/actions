from django.test import TestCase
from .utils import add

class AddFunctionTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        # self.assertEqual(add(2, 3), 7)  # This test will fail