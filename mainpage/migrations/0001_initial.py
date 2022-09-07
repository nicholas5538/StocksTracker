# Generated by Django 4.0.4 on 2022-06-29 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], default='BUY', max_length=4)),
                ('symbol', models.CharField(max_length=200)),
                ('transaction_date', models.DateField(default='29-06-2022')),
                ('share', models.PositiveIntegerField(default=0)),
                ('avg_price', models.PositiveIntegerField(default=0)),
                ('profit_loss', models.IntegerField(default=0)),
                ('cost_basis', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
