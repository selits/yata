# Generated by Django 2.0.5 on 2018-08-28 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0005_auto_20180828_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketdata',
            old_name='userId',
            new_name='sellId',
        ),
    ]
