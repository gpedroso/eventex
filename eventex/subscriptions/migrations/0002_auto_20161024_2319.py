# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 01:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('-created_at',), 'verbose_name': 'inscrição', 'verbose_name_plural': 'inscrições'},
        ),
        migrations.AddField(
            model_name='subscription',
            name='hashId',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telefone'),
        ),
    ]
