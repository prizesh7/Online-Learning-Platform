# Generated by Django 3.0.1 on 2020-02-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20200204_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='opt4',
            field=models.CharField(default='hello', max_length=100),
        ),
    ]