# Generated by Django 4.0.6 on 2022-08-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
