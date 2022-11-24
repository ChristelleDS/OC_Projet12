# Generated by Django 4.1.3 on 2022-11-23 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('contracts', '0002_alter_contract_salescontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='clients.client'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='payment_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]