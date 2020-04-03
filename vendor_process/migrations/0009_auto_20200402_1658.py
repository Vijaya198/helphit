# Generated by Django 2.2.2 on 2020-04-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_process', '0008_auto_20200401_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_address',
            name='door_street',
            field=models.CharField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='entity_name',
            field=models.CharField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='gstin',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='insurance_name',
            field=models.CharField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='insurance_no',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='locality',
            field=models.CharField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='uin',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='acc_holder_name',
            field=models.CharField(max_length=254),
        ),
    ]