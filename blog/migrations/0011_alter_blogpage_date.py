# Generated by Django 3.2.11 on 2022-03-11 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogpage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateTimeField(verbose_name='Fecha Post'),
        ),
    ]
