from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
	def test_form_has_fields(self):
		""" Form must have 4 fields """
		form = SubscriptionForm()
		expected = ['name', 'cpf', 'email', 'phone']
		self.assertSequenceEqual(expected, list(form.fields))

	def test_cpf_is_digit(self):
		""" CPF must only accept digits. """
		form = self.make_validated_forms(cpf='ABCD5678901')
		self.assertFormErrorCode(form, 'cpf', 'digits')

	def test_cpf_has_11_digits(self):
		""" CPF must have 11 digits """
		form = self.make_validated_forms(cpf='1234')
		self.assertFormErrorCode(form, 'cpf', 'length')

	def test_name_must_be_capitalized(self):
		""" name must be capitalized """
		form = self.make_validated_forms(name='GABRIEL pedroso')
		self.assertEqual('Gabriel Pedroso', form.cleaned_data['name'])

	def test_email_is_optional(self):
		""" email is optional """
		form = self.make_validated_forms(email='')
		self.assertFalse(form.errors)

	def test_phone_is_optional(self):
		""" phone is optional """
		form = self.make_validated_forms(phone='')
		self.assertFalse(form.errors)

	def test_must_inform_email_or_phone(self):
		""" email and phone are optiona, but one must be informed """
		form = self.make_validated_forms(email='', phone='')
		self.assertListEqual(['__all__'],list(form.errors))

	def test_must_inform_email_correct_or_phone(self):
		""" email and phone are optional, but one must be informed and email must be correct """
		form = self.make_validated_forms(email='123', phone='')
		self.assertListEqual(['email'],list(form.errors))

	def assertFormErrorCode(self, form, field, code):
		errors = form.errors.as_data()
		errors_list = errors[field]
		exception = errors_list[0]
		self.assertEqual(code, exception.code)


	def make_validated_forms(self, **kwargs):
		valid = dict(name='Gabriel Pedroso', cpf='12345678901', 
					email='gpedroso@gmail.com', phone='12-996582594')
		data = dict(valid, **kwargs)
		form = SubscriptionForm(data)
		form.is_valid()
		return form		