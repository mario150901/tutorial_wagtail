# Generated by Django 3.2.12 on 2022-03-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deporte',
            name='email',
            field=models.URLField(blank=True),
        ),
    ]
