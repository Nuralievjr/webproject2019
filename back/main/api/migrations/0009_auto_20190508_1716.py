# Generated by Django 2.2 on 2019-05-08 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_product_descrition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrition',
            new_name='description',
        ),
    ]
