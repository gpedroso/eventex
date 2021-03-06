from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
				name='Gabriel Pedroso',
				cpf='12345678901',
				email='gabriel@pedroso.net',
				phone='12-99654-2594'
				)
		self.obj.save()

	def test_create(self):
		self.assertTrue(Subscription.objects.exists())

	def test_created_at(self):
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_str(self):
		self.assertEqual('Gabriel Pedroso', str(self.obj))

	def test_paid_default_to_False(self):
		""" By default, paid must be false """
		self.assertEqual(False, self.obj.paid)