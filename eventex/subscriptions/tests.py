from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricao/ must return status code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """ HTML must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """ Html must contain CSRF """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """ Form must have 4 fields """
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

class SubscribePostTest(TestCase):
    def setUp(self):
        email = dict(name='Gabriel Pedroso', cpf='12345678901',
                    email='gpedroso@gmail.com', phone='12-99658-2594')
        self.resp = self.client.post('/inscricao/', email)

    def test_post(self):
        """ Valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        """ test send subscribe email"""
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        """ test subscribe email subject"""
        email = mail.outbox[0]
        expected = "Confirmação de inscrição"
        self.assertEqual(expected, email.subject)

    def test_subscription_email_from(self):
        """ test subscribe email subject"""
        email = mail.outbox[0]
        expected = "contato@eventex.com.br"
        self.assertEqual(expected, email.from_email)

    def test_subscription_email_to(self):
        """ test subscribe email subject"""
        email = mail.outbox[0]
        expected = ["contato@eventex.com.br", "gpedroso@gmail.com"]
        self.assertEqual(expected, email.to)

    def test_subscription_email_body(self):
        """ test subscribe email subject"""
        email = mail.outbox[0]
        self.assertIn('Gabriel Pedroso', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('gpedroso@gmail.com', email.body)
        self.assertIn('12-99658-2594', email.body)

class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class SubscribeSuccessMessage(TestCase):        
    def test_message(self):
        """ Test if show success message """
        email = dict(name='Gabriel Pedroso', cpf='12345678901',
                    email='gpedroso@gmail.com', phone='12-99658-2594')

        response = self.client.post('/inscricao/', email, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')