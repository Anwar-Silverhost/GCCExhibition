# Generated by Django 4.2.3 on 2023-07-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=240, null=True)),
                ('from_date', models.DateField(max_length=240, null=True)),
                ('to_date', models.DateField(max_length=240, null=True)),
                ('from_time', models.TimeField(max_length=240, null=True)),
                ('to_time', models.TimeField(max_length=240, null=True)),
                ('location', models.CharField(max_length=240, null=True)),
                ('status', models.CharField(max_length=240, null=True)),
                ('created_at', models.DateTimeField(max_length=240, null=True)),
            ],
        ),
    ]
