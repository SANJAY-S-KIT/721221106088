# Generated by Django 4.2.3 on 2024-03-20 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=20)),
                ('ownerName', models.CharField(max_length=20)),
                ('rollNo', models.CharField(max_length=10)),
                ('ownerEmail', models.EmailField(max_length=254, verbose_name='')),
                ('accessCode', models.CharField(max_length=6)),
            ],
        ),
    ]