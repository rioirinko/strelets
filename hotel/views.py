from rest_framework import generics
from strelets import settings
from .serializers import *
from .models import *
from django.core.mail import send_mail
from rest_framework.views import APIView


# class AcceptOrder(APIView):
#     queryset = OrderAcceptance.objects.filter(active=True)
#     serializers = OrderDetailedSerializer
#
#     def put(self, request, *args, **kwargs):
#         room_id = int(self.kwargs.get('room_id'))
#         Room.objects.filter(id=room_id).update(free=False)
#         action = self.request.data['action']
#         get_order = OrderAcceptance.objects.values_list('car_category', flat=True).get(pk=order_id)
#         user = UserProfile.objects.values_list('car_category', flat=True).get(user_id=request.user)
#         try:
#
#             update_serializer = OrderDetailedSerializer(data=request.data, partial=True)
#             if update_serializer.is_valid():
#                 if action == 'active':
#                     if get_order == user:
#
#                         OrderAcceptance.objects.filter(pk=order_id).update(active=request.data['active'],
#                                                                        driver=request.user)
#                         com = OrderAcceptance.objects.get(pk=order_id)
#                         UserProfile.objects.filter(user_id=request.user.id).update(
#                             balance=F('balance') - com.commission_from_price)
#                         return Response({"message": "Заказ успешно принят"}, status=status.HTTP_206_PARTIAL_CONTENT)
#                     else:
#                         return Response({'message': 'Вы не можете брать заказы не на свой тип авто'}, status=400)
#                 elif action == 'done':
#                     OrderAcceptance.objects.filter(pk=order_id).update(done=request.data['done'],
#                                                                        date_of_end=timezone.now())
#                     return Response({"message": "Заказ успешно выполнен"}, status=status.HTTP_206_PARTIAL_CONTENT)
#
#                 else:
#                     return Response(update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#             else:
#                 return Response({
#                     'Ошибка': 'Проверьте, соответствуют ли предоставленные поля правильному типу'
#                 }, status=status.HTTP_400_BAD_REQUEST)
#         except IntegrityError:
#             return Response({"Message": "Неправильные данные"}, status=status.HTTP_400_BAD_REQUEST)


class RoomViewSet(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailViewSet(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class ReviewViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ServicesViewSet(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def email_to_clients(self, request):
        subject = 'Гостиница'
        message = 'Номер забронирован!'
        email_from = settings.EMAIL_HOST_USER
        email = self.request.data['mail']
        send_mail(subject, message, email_from, email)