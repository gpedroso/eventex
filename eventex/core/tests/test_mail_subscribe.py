from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        email = dict(name='Gabriel Pedroso', cpf='12345678901',
                    email='gpedroso@gmail.com', phone='12-99658-2594')
        self.client.post(r('subscriptions:new'), email)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        """ test subscribe email subject"""
        expected = "Confirmação de inscrição"
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        """ test subscribe email subject"""
        expected = "contato@eventex.com.br"
        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        """ test subscribe email subject"""
        expected = ["contato@eventex.com.br", "gpedroso@gmail.com"]
        self.assertEqual(expected, self.email.to)

    def test_subscription_email_body(self):
        """ test subscribe email subject"""
        contents = ['Gabriel Pedroso', '12345678901', 'gpedroso@gmail.com','12-99658-2594',]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

