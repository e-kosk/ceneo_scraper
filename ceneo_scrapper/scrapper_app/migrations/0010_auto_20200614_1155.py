# Generated by Django 3.0.6 on 2020-06-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper_app', '0009_auto_20200611_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='rec_chart',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Recommendation chart'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='str_chart',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Stars chart'),
        ),
    ]
