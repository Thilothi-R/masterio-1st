# Generated by Django 3.2.3 on 2021-06-10 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0012_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('phone_nunmber', models.CharField(max_length=100)),
                ('messege', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='reg7',
        ),
    ]
