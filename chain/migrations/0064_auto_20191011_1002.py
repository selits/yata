# Generated by Django 2.0.5 on 2019-10-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0063_faction_createreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faction',
            name='createReport',
            field=models.BooleanField(default=False),
        ),
    ]
