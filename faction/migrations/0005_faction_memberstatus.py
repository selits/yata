# Generated by Django 3.0.1 on 2020-01-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0004_faction_posteropt'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='memberStatus',
            field=models.TextField(default='{}'),
        ),
    ]
