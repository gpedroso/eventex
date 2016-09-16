from django.test import TestCase

class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """ GET / must retun status_code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_useTemplate(self):
        """ Must use index.html template """
        self.assertTemplateUsed(self.response, 'index.html')