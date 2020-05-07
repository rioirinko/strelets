from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail

from hotel.decorators import threaded
from hotel.models import Room


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
    d1 = datetime.strptime(arrival, '%Y-%m-%d')
    d2 = datetime.strptime(departure, '%Y-%m-%d')
    date = d2 - d1
    # if request.user.is_authenticated():
    #     sum_ = ((date.days * price) * 10) / 100
    #     return sum_
    # else:
    sum_ = date.days * price
    return sum_


def update_room_status(number):
    upd = Room.objects.filter(pk=number).update(free=False)
    return upd