# Generated by Django 3.0.1 on 2020-03-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_auto_20200304_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='desp',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='query',
            name='desp',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
