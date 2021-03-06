# Generated by Django 2.1 on 2018-08-26 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('symbol', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=15)),
                ('percent_change_1h', models.DecimalField(decimal_places=5, max_digits=15)),
                ('percent_change_24h', models.DecimalField(decimal_places=5, max_digits=15)),
                ('percent_change_7d', models.DecimalField(decimal_places=5, max_digits=15)),
                ('market_cap', models.DecimalField(decimal_places=5, max_digits=15)),
                ('last_updated', models.DateTimeField(max_length=25, null=True)),
                ('cryptocurrency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Cryptocurrency')),
            ],
        ),
    ]
