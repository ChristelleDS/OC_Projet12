# Generated by Django 4.1.3 on 2022-11-24 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='company_name',
            new_name='company',
        ),
    ]
