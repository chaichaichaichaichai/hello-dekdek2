# Generated by Django 4.0.3 on 2022-03-24 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_options_alter_orderitem_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated',
        ),
    ]
