# Generated by Django 2.2.1 on 2019-05-26 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_remove_profile_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
