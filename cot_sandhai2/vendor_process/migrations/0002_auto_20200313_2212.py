# Generated by Django 2.2.2 on 2020-03-13 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_process', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_information',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_id', to=settings.AUTH_USER_MODEL),
        ),
    ]