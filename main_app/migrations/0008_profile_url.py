# Generated by Django 3.1.1 on 2020-11-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20201117_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
