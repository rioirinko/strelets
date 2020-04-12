from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from strelets import settings
from .serializers import *
from .models import *
from django.core.mail import send_mail
from rest_framework.views import APIView


# class FreeRoom(APIView):
#     queryset = Room.objects.filter(free=True)
#     serializers = RoomSerializer
#
#     def put(self, request, *args, **kwargs):
#         room_id = int(self.kwargs.get('room_id'))
#         Room.objects.filter(id=room_id).update(free=False)


class RoomViewSet(generics.ListAPIView):
    queryset = Room.objects.all().filter(free=True)
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['id']


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

