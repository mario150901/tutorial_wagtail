# Generated by Django 3.2.12 on 2022-02-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpage_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Footer',
            },
        ),
    ]
