# Generated by Django 4.2.3 on 2023-07-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('email', models.CharField(max_length=240, null=True)),
                ('mobile', models.CharField(max_length=240, null=True)),
                ('dob', models.CharField(max_length=240, null=True)),
                ('country', models.CharField(max_length=240, null=True)),
                ('nationality', models.CharField(max_length=240, null=True)),
                ('who', models.CharField(max_length=40, null=True)),
                ('school', models.CharField(max_length=40, null=True)),
                ('qualification', models.CharField(max_length=40, null=True)),
                ('study_abroad', models.CharField(max_length=40, null=True)),
                ('intrest', models.CharField(max_length=60, null=True)),
                ('others', models.CharField(max_length=60, null=True)),
                ('address', models.CharField(max_length=240, null=True)),
                ('school_ID', models.CharField(max_length=240, null=True)),
                ('event', models.CharField(max_length=240, null=True)),
                ('booking_ID', models.CharField(max_length=240, null=True)),
                ('event_exp', models.DateField(max_length=240, null=True)),
                ('QR', models.FileField(blank=True, null=True, upload_to='qrcodes/')),
                ('register_DT', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(max_length=240, null=True)),
            ],
        ),
    ]
