# Generated by Django 3.2.6 on 2021-08-30 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escarine_hol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='stars',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
