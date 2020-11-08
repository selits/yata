# Generated by Django 3.1.2 on 2020-11-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_analytics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='bandwidth',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='analytics',
            name='failed_requests',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='analytics',
            name='report_timestamp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='analytics',
            name='total_requests',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='analytics',
            name='unique_visitors',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='analytics',
            name='valid_requests',
            field=models.BigIntegerField(default=0),
        ),
    ]
