# Generated by Django 2.1 on 2018-08-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180828_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='market_cap',
            field=models.DecimalField(decimal_places=5, max_digits=15, null=True),
        ),
    ]
