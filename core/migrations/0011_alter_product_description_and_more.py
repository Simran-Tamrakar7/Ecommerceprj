# Generated by Django 4.2.16 on 2024-11-08 17:21

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='This is the product', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='I am a vendor', null=True),
        ),
    ]