# Generated by Django 3.2.3 on 2021-06-09 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0010_drop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drop',
            old_name='fileToUpload',
            new_name='image',
        ),
    ]
