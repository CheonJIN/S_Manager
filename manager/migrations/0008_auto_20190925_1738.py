# Generated by Django 2.0.13 on 2019-09-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20190923_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='regional_office',
            field=models.CharField(choices=[('SEOUL', 'Seoul'), ('DAEJEON', 'Daejeon'), ('BUSAN', 'Busan'), ('CHANGWON', 'Changwon'), ('GWHANGJU', 'Gwhanju')], max_length=15),
        ),
    ]
