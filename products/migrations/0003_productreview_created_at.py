# Generated by Django 3.2 on 2022-09-02 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220831_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_At'),
        ),
    ]
