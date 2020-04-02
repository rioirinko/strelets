from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'number', 'number_of_places', 'type_of_number', 'price', 'image')


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name', 'address', 'phone', 'passport', 'position')


class CustomerSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()

    def get_total_sum(self, request):
        d = request.date_of_departure - request.arrival_date
        sum = d.days * request.number.price
        return sum

    class Meta:
        model = Customer
        fields = ('id', 'name', 'passport', 'phone', 'address', 'number', 'employee',
                  'arrival_date', 'date_of_departure', 'total_sum')


class CleanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cleaning
        fields = ('id', 'number', 'employee', 'cleaning')


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'name', 'phone', 'number', 'arrival_date')


