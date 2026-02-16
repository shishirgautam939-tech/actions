from django.test import TestCase
from django.urls import reverse
from .utils import add


class AddFunctionTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        # self.assertEqual(add(2, 3), 7)  # This test will fail
        
class REgistrationFormTestCase(TestCase):
    def test_registration_form(self):
        response = self.client.get(reverse('registration:form'))
        #response = self.client.get(reverse('/registration/form/'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password')
        # Additional assertions can be added here to check the form content