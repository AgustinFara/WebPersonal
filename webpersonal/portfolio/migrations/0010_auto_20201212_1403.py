# Generated by Django 3.1.4 on 2020-12-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20201212_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='link para más información'),
        ),
    ]
