# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_oblasti'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oblasti',
            new_name='Oblast',
        ),
    ]
