# Generated by Django 3.0.4 on 2020-05-11 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0052_player_awardspinn'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmpReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0)),
                ('type', models.CharField(default='None', max_length=16)),
                ('req', models.TextField(default='{}')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Player')),
            ],
        ),
    ]