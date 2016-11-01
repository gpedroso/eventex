import uuid
from django.db import models

class Subscription(models.Model):
	name = models.CharField('Nome', max_length=100)
	cpf = models.CharField('CPF', max_length=11)
	email = models.EmailField('E-mail')
	phone = models.CharField('Telefone', max_length=20)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	hashId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

	# models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural='inscrições'
		verbose_name = 'inscrição'
		ordering = ('-created_at',)