# Generated by Django 4.2.13 on 2024-05-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0004_alter_school_bezeichnungzusatz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='bezeichnungzusatz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='profile',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='sprachen',
            field=models.TextField(blank=True, null=True),
        ),
    ]
