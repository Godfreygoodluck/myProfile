# Generated by Django 2.2.16 on 2021-05-14 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20210514_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='myskill',
            name='progresBar',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='myskill',
            name='percentage',
            field=models.CharField(max_length=10),
        ),
    ]