# Generated by Django 4.2.5 on 2023-09-17 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iha', '0005_kira_adet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kira',
            name='kirayan_üye',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='RentalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslangıc_tarih', models.DateField()),
                ('baslangıc_saat', models.TimeField()),
                ('bitiş_tarih', models.DateField()),
                ('bitiş_saat', models.TimeField()),
                ('Adet', models.IntegerField()),
                ('iha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iha.iha')),
                ('kirayan_üye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
