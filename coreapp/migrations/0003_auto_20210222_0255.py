# Generated by Django 3.1.7 on 2021-02-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_topfeatured'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='topfeatured',
            name='image',
            field=models.CharField(default='', max_length=300),
        ),
    ]
