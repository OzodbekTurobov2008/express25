# Generated by Django 5.1.2 on 2024-10-23 12:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('long', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('city', models.CharField(blank=True, max_length=35, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('street_address', models.CharField(blank=True, max_length=150, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
        ),
        migrations.CreateModel(
            name='PlasticCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('expiration_date', models.CharField(max_length=5)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='plastic_cards')),
            ],
            options={
                'verbose_name': 'PlasticCard',
                'verbose_name_plural': 'PlasticCards',
            },
        ),
    ]
