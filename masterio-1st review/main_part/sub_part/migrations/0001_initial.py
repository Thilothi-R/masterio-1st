# Generated by Django 3.2.3 on 2021-06-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
