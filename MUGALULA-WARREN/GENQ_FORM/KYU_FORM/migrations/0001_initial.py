# Generated by Django 4.2 on 2023-04-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=25)),
                ('LastName', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField()),
                ('GenderName', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ContactAndAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber1', models.IntegerField(max_length=20)),
                ('PhoneNumber2', models.IntegerField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=25)),
                ('StateOrDistrict', models.CharField(max_length=25)),
                ('Town', models.CharField(max_length=25)),
                ('ZipCode', models.IntegerField(max_length=6)),
            ],
        ),
    ]
