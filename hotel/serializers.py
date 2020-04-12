from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'name', 'price', 'image',)


class RoomDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'name', 'number_of_places', 'price', 'description', 'image', 'free',)


# class EmployeeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Employee
#         fields = ('id', 'name', 'address', 'phone', 'passport', 'position',)


# class CustomerSerializer(serializers.ModelSerializer):
#     total_sum = serializers.SerializerMethodField()
#
#     def get_total_sum(self, request):
#         d = request.date_of_departure - request.arrival_date
#         sum = d.days * request.number.price
#         return sum
#
#     class Meta:
#         model = Customer
#         fields = ('id', 'name', 'passport', 'phone', 'address', 'number', 'employee',
#                   'arrival_date', 'date_of_departure', 'total_sum')


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ('id', 'description',)


class BookingSerializer(serializers.ModelSerializer):
    # price = serializers.SerializerMethodField()
    #
    # def get_total_sum(self, request):
    #     d = request.date_of_departure - request.arrival_date
    #     sum = d.days * request.room.price
    #     return sum
    class Meta:
        model = Booking
        fields = ('id', 'name', 'number',  'phone', 'mail', 'service', 'arrival_date', 'date_of_departure', 'payment',
                  'price', 'comment',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'name', 'comment',)