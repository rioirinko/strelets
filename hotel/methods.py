from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import F

from hotel.decorators import threaded
from hotel.models import Room

User = get_user_model()

@threaded
def send_email_with_user(user, name, arrival_date, date_of_departure, sum_):
    head = "Бронь"
    message = 'Здравствуйте, {}.\n\n' \
              'Вы забронировали номер в отеле STRELETS, на дату {}. Дата выезда - {}.\n' \
              'Cумма за номер составит {}.\n'\
              'Ждём вас с нетерпением!\n'.format(name, arrival_date, date_of_departure, sum_)

    sender = str(settings.EMAIL_HOST_USER)
    sending = send_mail(head, message, sender, [str(user)])

    return sending == 1


def calculate_price(number, arrival, departure):
    price = Room.objects.values_list('price', flat=True).get(pk=number)
    d1 = datetime.strptime(arrival, '%d.%m.%Y')
    d2 = datetime.strptime(departure, '%d.%m.%Y')
    date = d2 - d1
    sum_ = date.days * price
    return sum_


def update_room_status(number):
    upd = Room.objects.filter(pk=number).update(free=False)
    return upd


def compare_date(arrival, departure):
    today = datetime.today()
    d1 = datetime.strptime(arrival, '%d.%m.%Y')
    d2 = datetime.strptime(departure, '%d.%m.%Y')
    now = datetime.strftime(today, '%d.%m.%Y')
    now_now = datetime.strptime(now, '%d.%m.%Y')
    if d1 > now_now and d2 > now_now:
        return True
    else:
        return False


def addition_user_points(user):
    points = User.objects.filter(username=user).update(
        points=F('points') + 10)
    print(points)
    return points

