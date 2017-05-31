# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20170530_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoafisica',
            name='fk_idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='login.Cliente', null=True),
            preserve_default=True,
        ),
    ]
