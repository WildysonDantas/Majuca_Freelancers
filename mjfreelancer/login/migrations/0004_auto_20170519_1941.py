# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.CharField(max_length=20, verbose_name=b'Data '),
            preserve_default=True,
        ),
    ]
