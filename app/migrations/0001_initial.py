# Generated by Django 4.2.3 on 2023-07-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=240, null=True)),
                ('description', models.CharField(max_length=240, null=True)),
                ('app_file', models.FileField(blank=True, null=True, upload_to='AppStore/')),
                ('download_count', models.CharField(max_length=240, null=True)),
                ('status', models.CharField(max_length=240, null=True)),
            ],
        ),
    ]
