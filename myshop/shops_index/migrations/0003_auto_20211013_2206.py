# Generated by Django 2.2 on 2021-10-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops_index', '0002_auto_20211010_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopscomm',
            name='comm_en',
            field=models.CharField(max_length=10000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='shopscomm',
            name='comm_ru',
            field=models.CharField(max_length=10000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]