# Generated by Django 3.2.24 on 2024-02-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='edited_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.CharField(default='Not Specified', max_length=500, verbose_name='ingredients'),
        ),
    ]
