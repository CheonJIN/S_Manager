# Generated by Django 2.0.13 on 2019-09-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20190923_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='regional_office',
            field=models.CharField(choices=[('SEOUL', 'Seoul'), ('DAEJEAN', 'Daejean'), ('BUSAN', 'Busan'), ('CHANGWON', 'Changwon'), ('GWHANGJU', 'Gwhanju')], max_length=15),
        ),
    ]