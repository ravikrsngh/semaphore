# Generated by Django 2.0.2 on 2019-09-27 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190927_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketer',
            name='boss',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='marketer',
            name='t_reg',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marketer',
            name='undercover',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='college',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
