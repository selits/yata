# Generated by Django 3.0.4 on 2020-04-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0042_auto_20200402_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='verifyWeeklyCheck',
            field=models.BooleanField(default=False, help_text="Do automatic '!checkFactions force' every 7x24 hours"),
        ),
        migrations.AddField(
            model_name='guild',
            name='verifyWeeklyVerify',
            field=models.BooleanField(default=False, help_text="Do automatic '!verifyAll force' every 7x24 hours"),
        ),
        migrations.AlterField(
            model_name='guild',
            name='verifyDailyCheck',
            field=models.BooleanField(default=False, help_text="Do automatic '!checkFactions force' every 24 hours"),
        ),
        migrations.AlterField(
            model_name='guild',
            name='verifyDailyVerify',
            field=models.BooleanField(default=False, help_text="Do automatic '!verifyAll force' every 24 hours"),
        ),
    ]
