# Generated by Django 4.2.3 on 2023-10-27 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imported', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imported',
            options={'permissions': [('can_write_imported', 'Can write Imported')]},
        ),
    ]