# Generated by Django 3.1 on 2021-05-09 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210508_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='order',
            new_name='orders',
        ),
    ]
