# Generated by Django 3.2.6 on 2021-08-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('country_name', models.CharField(max_length=30)),
                ('city_name', models.CharField(max_length=30)),
                ('title', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
