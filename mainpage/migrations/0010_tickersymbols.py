# Generated by Django 4.0.4 on 2022-07-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_alter_portfolio_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TickerSymbols',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickersymbols', models.CharField(max_length=10)),
            ],
        ),
    ]
