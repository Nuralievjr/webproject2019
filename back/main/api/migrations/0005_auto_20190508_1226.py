# Generated by Django 2.2 on 2019-05-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_contactmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.CharField(max_length=200),
        ),
    ]