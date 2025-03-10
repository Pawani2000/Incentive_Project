# Generated by Django 5.1.7 on 2025-03-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_incentive', '0002_paymentstage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BBPackagePCR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_type', models.CharField(max_length=50)),
                ('order_type', models.CharField(max_length=50)),
                ('tariff_id', models.CharField(blank=True, max_length=50, null=True)),
                ('tariff_name', models.CharField(blank=True, max_length=50, null=True)),
                ('pcr', models.FloatField(blank=True, null=True)),
                ('additional_cost', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bb_package_pcr',
            },
        ),
        migrations.CreateModel(
            name='BearerPCR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('speed', models.CharField(max_length=50)),
                ('service_order_type', models.CharField(max_length=50)),
                ('with_bb_router', models.CharField(blank=True, max_length=50, null=True)),
                ('without_bb_router', models.CharField(blank=True, max_length=50, null=True)),
                ('tariff_id', models.CharField(max_length=50)),
                ('tariff_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bearer_pcr',
            },
        ),
        migrations.CreateModel(
            name='ExclusionPackage',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tariff_id', models.CharField(max_length=50)),
                ('tariff_name_pack', models.CharField(max_length=50)),
                ('exclusion', models.BooleanField()),
                ('created_date', models.DateField()),
                ('created_user', models.CharField(max_length=50)),
                ('updated_date', models.DateField(blank=True, null=True)),
                ('updated_user', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'exclusion_package',
            },
        ),
        migrations.CreateModel(
            name='PEORates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_type', models.CharField(max_length=50)),
                ('order_type', models.CharField(max_length=50)),
                ('tariff_id', models.CharField(blank=True, max_length=50, null=True)),
                ('tariff_name', models.CharField(blank=True, max_length=50, null=True)),
                ('pcr', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'peo_rates',
            },
        ),
        migrations.CreateModel(
            name='SlabLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slab_level', models.CharField(max_length=50)),
                ('upper_range', models.DecimalField(decimal_places=2, max_digits=15)),
                ('lower_range', models.DecimalField(decimal_places=2, max_digits=15)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_user', models.CharField(max_length=50)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('updated_user', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'slab_level',
            },
        ),
    ]
