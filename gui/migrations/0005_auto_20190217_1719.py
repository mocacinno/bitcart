# Generated by Django 2.1.7 on 2019-02-17 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0004_auto_20190217_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='decription',
            new_name='description',
        ),
    ]