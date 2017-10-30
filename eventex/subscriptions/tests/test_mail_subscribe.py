from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Cristiano Reis', cpf='11111111111',
                    email='cristianoreisnascimento@gmail.com', phone='22-99721-5080')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'cristianoreisnascimento@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = [
            'Cristiano Reis',
            '11111111111',
            'cristianoreisnascimento@gmail.com',
            '22-99721-5080',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)