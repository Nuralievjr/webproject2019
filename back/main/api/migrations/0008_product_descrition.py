# Generated by Django 2.2 on 2019-05-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_product_decription'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descrition',
            field=models.CharField(default='Опсиание еще не добавлено!', max_length=400),
        ),
    ]
