# Generated by Django 3.1 on 2021-05-09 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210508_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='orders',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
