# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20170530_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoafisica',
            name='fk_idCliente',
            field=models.OneToOneField(to='login.Cliente'),
            preserve_default=True,
        ),
    ]
