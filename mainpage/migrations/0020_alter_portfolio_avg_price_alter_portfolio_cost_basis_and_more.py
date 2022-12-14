# Generated by Django 4.0.4 on 2022-08-06 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0019_transaction_commission_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='avg_price',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='cost_basis',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='current_value',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='profit_loss',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='total_shares',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='avg_price',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='cost_basis',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='share',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
