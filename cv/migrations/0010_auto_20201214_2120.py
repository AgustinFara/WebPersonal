# Generated by Django 3.1.4 on 2020-12-15 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_auto_20201214_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_image',
            new_name='image',
        ),
        migrations.AddField(
            model_name='client',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
    ]
