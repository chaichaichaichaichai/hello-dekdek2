# Generated by Django 4.0.3 on 2022-03-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_cart_options_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('date_added',), 'verbose_name': 'ตระกร้าสินค้า', 'verbose_name_plural': 'ตระกร้าสินค้า'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'รายการสินค้าในตระกร้า', 'verbose_name_plural': 'รายการสินค้าในตระกร้า'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='token',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='created',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='updated',
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterModelTable(
            name='order',
            table=None,
        ),
    ]
