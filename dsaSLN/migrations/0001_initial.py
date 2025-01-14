# Generated by Django 5.0.7 on 2024-08-16 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DSA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsa_registerid', models.CharField(max_length=100)),
                ('dsa_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DSA_Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_applicationId', models.CharField(max_length=100)),
                ('loan_type', models.CharField(max_length=100, null=True)),
                ('dsa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dsa', to='dsaSLN.dsa')),
            ],
        ),
    ]
