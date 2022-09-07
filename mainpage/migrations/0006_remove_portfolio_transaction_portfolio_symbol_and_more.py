# Generated by Django 4.0.4 on 2022-07-10 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainpage', '0005_alter_portfolio_transaction_alter_portfolio_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='transaction',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='symbol',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
