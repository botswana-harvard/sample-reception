# Generated by Django 2.0.6 on 2018-06-11 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_reception', '0004_auto_20180610_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectrequisition',
            name='requisition_identifier',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Requisition Id'),
        ),
        migrations.AlterField(
            model_name='subjectrequisition',
            name='requisition_identifier',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Requisition Id'),
        ),
    ]