# Generated by Django 2.1.7 on 2019-03-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0014_product_bitcoin_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bitcoin_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
