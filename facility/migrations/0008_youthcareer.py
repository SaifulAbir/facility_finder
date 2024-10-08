# Generated by Django 4.2.13 on 2024-05-27 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0007_socialwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouthCareer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField()),
                ('category', models.CharField(max_length=80)),
                ('traeger', models.TextField(blank=True, null=True)),
                ('leistungen', models.CharField(blank=True, max_length=255, null=True)),
                ('bezeichnung', models.CharField(blank=True, max_length=255, null=True)),
                ('kurzbezeichnung', models.CharField(blank=True, max_length=255, null=True)),
                ('strasse', models.CharField(blank=True, max_length=250, null=True)),
                ('plz', models.CharField(blank=True, max_length=150, null=True)),
                ('ort', models.CharField(blank=True, max_length=150, null=True)),
                ('telefon', models.CharField(blank=True, max_length=150, null=True)),
                ('fax', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'youth_careers',
            },
        ),
    ]
