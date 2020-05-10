from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .methods import send_email_with_user, update_room_status, calculate_price, compare_date, addition_user_points
from .serializers import *

User = get_user_model()


class RoomViewSet(generics.ListAPIView):
    queryset = Room.objects.all().filter(free=True)
    serializer_class = RoomSerializer
    ordering = ['id']
    permission_classes = [AllowAny]


class RoomDetailViewSet(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    permission_classes = [AllowAny]


class CreateReviewViewSet(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)


class ReviewViewSet(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]


class ServicesViewSet(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [AllowAny]


class QuestionsViewSet(generics.CreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = [AllowAny]


class BookingViewSet(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            if compare_date(request.data['arrival_date'], request.data['date_of_departure']):
                sum_ = calculate_price(request.data['number'], request.data['arrival_date'],
                                       request.data['date_of_departure'])
                Booking.objects.create(user=request.user, price=sum_, **serializer.validated_data)
                update_room_status(request.data['number'])
                send_email_with_user(request.data['mail'], request.data['name'],
                                     request.data['arrival_date'], request.data['date_of_departure'], sum_)
                addition_user_points(request.user)
            else:
                return Response({"message": "Не валидная дата"}, status=400)
        except ValidationError as e:
            return Response({'message': e.detail}, status=400)

        return Response({'Message': f'Сумма за номер составит {sum_}'}, status=status.HTTP_201_CREATED)


class UserBookingViewSet(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(user=request.user)
        self.queryset = queryset
        self.serializer_class = BookingSerializer
        return super().list(request, *args, **kwargs)
