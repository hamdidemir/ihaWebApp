# Generated by Django 4.2.5 on 2023-09-17 20:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iha', '0006_alter_kira_kirayan_üye_rentalhistory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RentalHistory',
            new_name='KiralıkTarihi',
        ),
    ]
