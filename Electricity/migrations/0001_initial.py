# Generated by Django 4.1.5 on 2023-04-28 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inversor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('local', models.CharField(blank=True, max_length=256, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('energia_diaV2', models.FloatField(blank=True, null=True)),
                ('energia_ano', models.FloatField(blank=True, null=True)),
                ('energia_total', models.FloatField(blank=True, null=True)),
                ('potenciav2', models.FloatField(blank=True, null=True)),
                ('power_led', models.BooleanField(default=False)),
                ('solarnet_led', models.BooleanField(default=False)),
                ('solarweb_led', models.BooleanField(default=False)),
                ('painel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Electricity.inversor')),
            ],
        ),
    ]
