import uuid
from django.db import models
from eventex.subscriptions.validators import validate_cpf

class Subscription(models.Model):
	name = models.CharField('Nome', max_length=100)
	cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
	email = models.EmailField('E-mail', blank=True)
	phone = models.CharField('Telefone', max_length=20, blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	hashId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
	paid = models.BooleanField('Pago', default=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural='inscrições'
		verbose_name = 'inscrição'
		ordering = ('-created_at',)