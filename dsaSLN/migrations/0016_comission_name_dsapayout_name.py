# Generated by Django 5.0.7 on 2024-10-09 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsaSLN', '0015_alter_dsa_dsa_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comission',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dsapayout',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
