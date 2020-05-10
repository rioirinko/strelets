from django.conf.urls import url
from hotel import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from strelets import settings

app_name = 'hotel'

urlpatterns = [
    url(r'^room/$', views.RoomViewSet.as_view(), name='Room'),
    url(r'^room/(?P<pk>[0-9]+)/$', views.RoomDetailViewSet.as_view()),
    url(r'^services/$', views.ServicesViewSet.as_view(), name='Services'),
    url(r'^review/$', views.ReviewViewSet.as_view(), name='Review'),
    url(r'^createreview/$', views.CreateReviewViewSet.as_view(), name='Create review'),
    url(r'^booking/$', views.BookingViewSet.as_view(), name='Booking'),
    url(r'^userbooking/$', views.UserBookingViewSet.as_view(), name="Booking user"),
    url(r'^question/$', views.QuestionsViewSet.as_view(), name='Questions')
]
urlpatterns = format_suffix_patterns(urlpatterns)