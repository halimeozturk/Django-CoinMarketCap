# Generated by Django 2.1 on 2018-08-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180828_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='market_cap',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=15, null=True),
        ),
    ]
