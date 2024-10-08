# Generated by Django 4.2.13 on 2024-06-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_favorite_facility_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='home_address_category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='home_address_id',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='street_house_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
