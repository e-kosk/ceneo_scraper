# Generated by Django 3.0.7 on 2020-06-06 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper_app', '0006_productmodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opinionmodel',
            old_name='recomendation',
            new_name='recommendation',
        ),
    ]