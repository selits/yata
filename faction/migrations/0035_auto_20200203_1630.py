# Generated by Django 3.0.1 on 2020-02-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0034_auto_20200203_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attackchain',
            name='attacker_factionname',
            field=models.CharField(blank=True, default='attacker_factionname', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='attackchain',
            name='defender_factionname',
            field=models.CharField(blank=True, default='defender_factionname', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='attackchain',
            name='result',
            field=models.CharField(default='result', max_length=64),
        ),
        migrations.AlterField(
            model_name='attackreport',
            name='attacker_factionname',
            field=models.CharField(blank=True, default='attacker_factionname', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='attackreport',
            name='defender_factionname',
            field=models.CharField(blank=True, default='defender_factionname', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='attackreport',
            name='result',
            field=models.CharField(default='result', max_length=64),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='stat',
            field=models.CharField(default='stat', max_length=64),
        ),
        migrations.AlterField(
            model_name='faction',
            name='name',
            field=models.CharField(default='MyFaction', max_length=64),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='wall',
            name='attackerFactionName',
            field=models.CharField(default='AttackFaction', max_length=64),
        ),
        migrations.AlterField(
            model_name='wall',
            name='defenderFactionName',
            field=models.CharField(default='DefendFaction', max_length=64),
        ),
    ]