from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'name', 'price', 'image',)


class RoomDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'name', 'family_apartment', 'bathroom', 'number_of_places', 'mini_bar', 'tv',
                  'air_conditioning', 'wi_fi', 'refrigerator', 'pets', 'price', 'description', 'image', 'free',)


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ('id', 'description',)


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'user', 'name', 'number',  'phone', 'passport', 'mail', 'service', 'arrival_date',
                  'date_of_departure', 'comment',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'name', 'comment',)


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('id', 'name', 'mail', 'message_subject', 'question',)
