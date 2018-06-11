# Generated by Django 2.0.6 on 2018-06-10 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sample_reception', '0002_auto_20180610_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubjectrequisition',
            name='receive_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='historicalsubjectrequisition',
            name='site_code',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='historicalsubjectrequisition',
            name='specimen_condition',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='subjectrequisition',
            name='receive_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='subjectrequisition',
            name='site_code',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='subjectrequisition',
            name='specimen_condition',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
