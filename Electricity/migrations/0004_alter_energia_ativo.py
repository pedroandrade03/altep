# Generated by Django 4.1.5 on 2023-04-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electricity', '0003_energia_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energia',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]
