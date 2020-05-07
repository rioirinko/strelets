from django.conf.urls import re_path
from .views import RegistrationAPIView, LoginAPIView

app_name = 'base_user'

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]