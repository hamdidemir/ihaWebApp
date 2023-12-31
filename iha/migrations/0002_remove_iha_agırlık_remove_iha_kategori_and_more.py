# Generated by Django 4.2.5 on 2023-09-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iha', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iha',
            name='Agırlık',
        ),
        migrations.RemoveField(
            model_name='iha',
            name='Kategori',
        ),
        migrations.RemoveField(
            model_name='kira',
            name='saat',
        ),
        migrations.RemoveField(
            model_name='kira',
            name='tarih',
        ),
        migrations.AddField(
            model_name='iha',
            name='Faydalı_yük',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iha',
            name='Havada_kalma_suresi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iha',
            name='Kanat_acıklıgı',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='iha',
            name='Maksimum_kalkıs_agırlıgı',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kira',
            name='baslangıc_saat',
            field=models.TimeField(default='12:00:00'),
        ),
        migrations.AddField(
            model_name='kira',
            name='baslangıc_tarih',
            field=models.DateField(default='2010-12-31'),
        ),
        migrations.AddField(
            model_name='kira',
            name='bitiş_saat',
            field=models.TimeField(default='12:00:00'),
        ),
        migrations.AddField(
            model_name='kira',
            name='bitiş_tarih',
            field=models.DateField(default='2050-12-31'),
        ),
    ]
