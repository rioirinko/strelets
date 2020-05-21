from django.conf.urls import re_path, url
from .views import RegistrationAPIView, LoginAPIView, InfoUserViewSet

app_name = 'base_user'

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    url(r'^userinfo/$', InfoUserViewSet.as_view(), name='Q'),
]