# Generated by Django 4.2.3 on 2023-10-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_ahdaa_date_ahdaa_alter_mostakhlas_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='letter_of_guarantee',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]