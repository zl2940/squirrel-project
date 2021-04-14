# Generated by Django 3.0.7 on 2021-04-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='X',
            field=models.DecimalField(blank=True, decimal_places=15, help_text='Longitude', max_digits=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Y',
            field=models.DecimalField(blank=True, decimal_places=15, help_text='Latitude', max_digits=100),
        ),
    ]