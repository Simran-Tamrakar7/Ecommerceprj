# Generated by Django 4.2.16 on 2024-11-07 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_product_tags_product_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Vendor',
            new_name='vendor',
        ),
    ]
