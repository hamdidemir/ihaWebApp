# Generated by Django 4.2.5 on 2023-09-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iha', '0008_rename_kiralıktarihi_rentalhistory_alter_kira_iha'),
    ]

    operations = [
        migrations.AddField(
            model_name='iha',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='iha_images/'),
        ),
    ]
