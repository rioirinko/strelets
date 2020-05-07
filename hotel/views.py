from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .methods import send_email_with_user, update_room_status, calculate_price
from .serializers import *
from .models import *


class RoomViewSet(generics.ListAPIView):
    queryset = Room.objects.all().filter(free=True)
    serializer_class = RoomSerializer
    ordering = ['id']


class RoomDetailViewSet(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class ReviewViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)


class ServicesViewSet(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class QuestionsViewSet(generics.CreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class BookingViewSet(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            update_room_status(request.data['number'])
            sum_ = calculate_price(request.data['number'], request.data['arrival_date'],
                                   request.data['date_of_departure'])
            send_email_with_user(request.data['mail'], request.data['name'],
                                 request.data['arrival_date'], request.data['date_of_departure'], sum_)

        except ValidationError as e:
            return Response({'message': e.detail}, status=400)

        self.perform_create(serializer)
        return Response({'Message': f'Сумма за номер составит {sum_}'}, status=status.HTTP_201_CREATED)