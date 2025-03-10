# Generated by Django 5.1.7 on 2025-03-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiaSoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('sales_type', models.CharField(max_length=50)),
                ('service_type', models.CharField(max_length=50)),
                ('order_type', models.CharField(max_length=50)),
                ('slab_eligibility', models.BooleanField()),
                ('pcr_eligibility', models.BooleanField(db_column='PCR_ELI')),
                ('created_date', models.DateField()),
                ('created_user', models.CharField(max_length=50)),
                ('updated_date', models.DateField(blank=True, null=True)),
                ('updated_user', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sia_so_types',
            },
        ),
    ]
