# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170519_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Email', models.CharField(max_length=50, verbose_name=b'Email ')),
                ('data', models.CharField(max_length=10, verbose_name=b'Data ')),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome ')),
                ('sexo', models.CharField(max_length=50, verbose_name=b'Sexo: ', choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')])),
                ('mensagem', models.CharField(max_length=500, verbose_name=b'mensagem ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
