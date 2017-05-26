# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=70, blank=True)),
                ('Email', models.EmailField(max_length=30, blank=True)),
                ('Foto', models.CharField(max_length=100, null=True)),
                ('Senha', models.CharField(max_length=30, blank=True)),
                ('Telefone', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=70, blank=True)),
                ('Email', models.EmailField(max_length=20, blank=True)),
                ('Endereco', models.CharField(max_length=100, blank=True)),
                ('Cidade', models.CharField(max_length=30, blank=True)),
                ('Estado', models.CharField(max_length=20, blank=True)),
                ('CPF', models.CharField(unique=True, max_length=11, blank=True)),
                ('Agencia', models.CharField(max_length=6, blank=True)),
                ('Banco', models.CharField(max_length=25, blank=True)),
                ('Conta', models.CharField(max_length=10, blank=True)),
                ('Telefone', models.CharField(max_length=10, blank=True)),
                ('Senha', models.CharField(max_length=25, blank=True)),
                ('Especialidade', models.CharField(max_length=150)),
                ('SobreMim', models.CharField(max_length=150)),
                ('NotaAvaliativa', models.IntegerField()),
                ('Foto', models.CharField(max_length=100, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('CPF', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('fk_idCliente', models.ForeignKey(to='login.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('CNPJ', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('Cliente', models.ForeignKey(to='login.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=70, blank=True)),
                ('AreaProjeto', models.CharField(max_length=70, blank=True)),
                ('DataPublicacao', models.DateTimeField(null=True, blank=True)),
                ('DataInicio', models.DateTimeField(null=True, blank=True)),
                ('DataFim', models.DateTimeField(null=True, blank=True)),
                ('Preco', models.FloatField(null=True, blank=True)),
                ('Descricao', models.CharField(max_length=200, blank=True)),
                ('cliente', models.ForeignKey(default=1, to='login.Cliente')),
                ('idFreelancer', models.ForeignKey(default=1, to='login.Freelancer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='login',
            name='login_email',
            field=models.CharField(max_length=50, verbose_name=b'Email '),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='login',
            name='login_senha',
            field=models.CharField(max_length=30, verbose_name=b'Senha '),
            preserve_default=True,
        ),
    ]
