# Generated by Django 4.0.4 on 2022-07-16 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0014_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_type',
            new_name='transaction',
        ),
    ]
