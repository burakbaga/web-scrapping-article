# Generated by Django 2.0.13 on 2019-06-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koseyazi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birgun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=100)),
                ('baslik', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cumhuriyet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=100)),
                ('baslik', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Milliyet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=100)),
                ('baslik', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
            ],
        ),
    ]
