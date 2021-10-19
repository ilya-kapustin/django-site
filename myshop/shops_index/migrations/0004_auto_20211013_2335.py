# Generated by Django 2.2 on 2021-10-13 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops_index', '0003_auto_20211013_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shops',
            options={'verbose_name': 'good', 'verbose_name_plural': 'goods'},
        ),
        migrations.AlterModelOptions(
            name='shopscomm',
            options={'verbose_name': 'comm', 'verbose_name_plural': 'comms'},
        ),
        migrations.AlterModelOptions(
            name='shopsgroup',
            options={'verbose_name': 'group', 'verbose_name_plural': 'groups'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
        migrations.AlterField(
            model_name='shops',
            name='code_thing',
            field=models.IntegerField(default=0, verbose_name='code_thing'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='description',
            field=models.CharField(max_length=10000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='description_en',
            field=models.CharField(max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='description_ru',
            field=models.CharField(max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ShopsGroup', to='shops_index.ShopsGroup', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='img',
            field=models.ImageField(upload_to='images', verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='price',
            field=models.FloatField(default=0, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='status',
            field=models.CharField(choices=[('d', 'Черновик'), ('r', 'Снято с продаж'), ('p', 'Продается')], default='d', max_length=1, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='tags',
            field=models.ManyToManyField(blank=True, to='shops_index.Tag', verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='views_count'),
        ),
        migrations.AlterField(
            model_name='shopscomm',
            name='author',
            field=models.CharField(max_length=255, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='shopscomm',
            name='comm',
            field=models.CharField(max_length=10000, verbose_name='comm'),
        ),
        migrations.AlterField(
            model_name='shopscomm',
            name='comm_en',
            field=models.CharField(max_length=10000, null=True, verbose_name='comm'),
        ),
        migrations.AlterField(
            model_name='shopscomm',
            name='comm_ru',
            field=models.CharField(max_length=10000, null=True, verbose_name='comm'),
        ),
        migrations.AlterField(
            model_name='shopscomm',
            name='grade',
            field=models.FloatField(default=0, verbose_name='grade'),
        ),
        migrations.AlterField(
            model_name='shopscomm',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Shops', to='shops_index.ShopsGroup', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='shopscomm',
            name='shops',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ShopsGroup', to='shops_index.Shops', verbose_name='shops'),
        ),
        migrations.AlterField(
            model_name='shopscomm',
            name='status',
            field=models.CharField(choices=[('r', 'Удалено администратором'), ('p', 'Опубликованно')], default='d', max_length=1, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='shopsgroup',
            name='description',
            field=models.CharField(max_length=10000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='shopsgroup',
            name='description_en',
            field=models.CharField(max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='shopsgroup',
            name='description_ru',
            field=models.CharField(max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='shopsgroup',
            name='img',
            field=models.ImageField(upload_to='images', verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='shopsgroup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='shopsgroup',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='shopsgroup',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=255, verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='tag'),
        ),
    ]