# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_remove_contato_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoafisica',
            name='fk_idCliente',
            field=models.ForeignKey(to='login.Cliente', on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
    ]
