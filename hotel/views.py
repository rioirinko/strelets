from rest_framework import generics
from .serializers import *
from .models import *


class CustomerViewSet(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class RoomViewSet(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class EmployeeViewSet(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CleanViewSet(generics.ListCreateAPIView):
    queryset = Cleaning.objects.all()
    serializer_class = CleanSerializer


class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer