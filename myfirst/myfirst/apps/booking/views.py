from django.shortcuts import render
from django.http import HttpResponse
import django.utils.timezone as timezone
from datetime import timedelta, datetime

from django.conf import settings
from django.core.mail import send_mail, send_mass_mail

from .models import Hall, Computer, Reservation

#Отправка Email
def messages(em, name, time, pc):
	datatuple = (
    	('Региcтрация брони в RubickPC', f'Здраствуйте {name} вами забронирован компьютер под номером {pc} на {time}, ждем вас', settings.EMAIL_HOST_USER, [em]),
    	('Сообщение связанное с сайтом', f'Сообщение оправлено пользовотелю {name}', settings.EMAIL_HOST_USER, ['akulenko_874@mail.ru']),
	)
	send_mass_mail(datatuple)

#Страница выбора места
def index(request):
	c = Computer.objects.get(id=1)
	print(c.busy)
	timez = timezone.localtime(timezone.now())
	print(timez)
	if request.POST:
		id_pc = int(request.POST.get("id_pc"))
		fio = request.POST.get("fio")
		dtime = request.POST.get("dtime")
		time = request.POST.get("time")
		email = request.POST.get("email")
		tel = request.POST.get("tel")
		messages(email, fio, dtime, id_pc)

		print(id_pc, fio, dtime, time, email, tel)
		Reservation.objects.create(computer=Computer.objects.get(id=id_pc), fio=fio, booking_time=dtime,
			                    duration=time, email=email, phone_number=tel)
    
	#Освобождаем места
	for i in Computer.objects.filter(busy=False):
		for j in Reservation.objects.filter(booking_time__day != timez.day):
			i.busy = True
			i.save()

		for j in Reservation.objects.filter(booking_time__year = timez.year,
			                                booking_time__month = timez.month,
			                                booking_time__day = timez.day):
            #Время продолжительности d_h:d_m {00:00}
			d_h = str(j.duration)[:2]
			d_m = str(j.duration)[3:5]

			if timez > (j.booking_time + timedelta(hours=int(d_h), minutes=int(d_m))):
				i.busy = True
				i.save()

	#Занимаем места
	for i in Reservation.objects.filter(booking_time__year = timez.year,
			                                booking_time__month = timez.month,
			                                booking_time__day = timez.day):
		#Время продолжительности d_h:d_m {00:00}
		d_h = str(i.duration)[:2]
		d_m = str(i.duration)[3:5]

		if timez >= (i.booking_time + timedelta(seconds=1)) and timez <= (i.booking_time + timedelta(hours=int(d_h), minutes=int(d_m))):
			c = i.computer
			c.busy = False
			c.save()

	regular = Computer.objects.all()[:20]
	unusual = Computer.objects.all()[20:35]
	vip = Computer.objects.all()[35:40]

	return render(request, 'booking/index.html', {'regular': regular, 'unusual': unusual, 'vip': vip})

#Страница регистрации
def application(request, pc_id):
	return render(request, 'booking/html/application.html', {'pc': pc_id})