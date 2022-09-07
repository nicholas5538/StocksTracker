# Generated by Django 4.0.4 on 2022-07-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0017_portfolio_avg_price_portfolio_cost_basis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='avg_price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='cost_basis',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='avg_price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='cost_basis',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
