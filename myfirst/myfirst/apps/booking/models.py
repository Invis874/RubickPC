from django.db import models

class Hall(models.Model):
	hall_title = models.CharField('Название зала', max_length = 50)
	quantity_pc = models.IntegerField('Количество PC')

	def __str__(self):
		return self.hall_title

	class Meta:
		verbose_name = 'Зал'
		verbose_name_plural = 'Залы'

class Computer(models.Model):
	hall = models.ForeignKey(Hall, on_delete = models.CASCADE)
	cpu = models.CharField('Процессор PC', max_length = 250)
	video_card = models.CharField('Видеокарта PC', max_length = 250)
	ram = models.CharField('Оперативная память PC', max_length = 250)
	busy = models.BooleanField('Занятость PC', default = 0)

	class Meta:
		verbose_name = 'Компьютер'
		verbose_name_plural = 'Компьютеры'

class Reservation(models.Model):
	computer = models.ForeignKey(Computer, on_delete = models.CASCADE)
	fio = models.CharField('ФИО клиента', max_length = 200)
	booking_time = models.DateTimeField('Время брони')
	duration = models.TimeField('Продолжительность')
	email = models.CharField('Email', max_length = 250)
	phone_number = models.CharField('Телефон', max_length = 12)

	def __str__(self):
		return self.fio

	class Meta:
		verbose_name = 'Бронь'
		verbose_name_plural = 'Брони'