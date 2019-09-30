# Generated by Django 2.0.13 on 2019-09-27 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20190925_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('host', models.CharField(max_length=20)),
                ('lum_target', models.CharField(max_length=20)),
                ('dsls_target', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('module', models.CharField(max_length=100)),
                ('memo', models.CharField(max_length=200)),
                ('explaration_date', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licenses', to='manager.Company')),
            ],
        ),
    ]