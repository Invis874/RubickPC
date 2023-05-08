# Generated by Django 4.1.7 on 2023-04-02 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_title', models.CharField(max_length=50, verbose_name='Название зала')),
                ('quantity_pc', models.IntegerField(verbose_name='Количество PC')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.CharField(max_length=250, verbose_name='Процессор PC')),
                ('video_card', models.CharField(max_length=250, verbose_name='Видеокарта PC')),
                ('ram', models.CharField(max_length=250, verbose_name='Оперативная память PC')),
                ('busy', models.BooleanField(default=0, verbose_name='Занятость PC')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО клиента')),
                ('booking_time', models.DateTimeField(verbose_name='Время брони')),
                ('duration', models.TimeField(verbose_name='Продолжительность')),
                ('email', models.CharField(max_length=250, verbose_name='email')),
                ('phone_number', models.CharField(max_length=12, verbose_name='email')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.computer')),
            ],
        ),
    ]
