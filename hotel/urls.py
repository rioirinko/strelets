from django.conf.urls import url
from hotel import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static

from strelets import settings

urlpatterns = [
    url(r'^room/$', views.RoomViewSet.as_view(), name='Room'),
    url(r'^room/(?P<pk>[0-9]+)/$', views.RoomDetailViewSet.as_view()),
    url(r'^services/$', views.ServicesViewSet.as_view(), name='Services'),
    url(r'^review/$', views.ReviewViewSet.as_view(), name='Review'),
    url(r'^booking/$', views.BookingViewSet.as_view(), name='Booking'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

