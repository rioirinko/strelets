"""strelets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from hotel import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^customer/$', views.CustomerViewSet.as_view(), name='Customer'),
    url(r'^room/$', views.RoomViewSet.as_view(), name='Room'),
    url(r'^clean/$', views.CleanViewSet.as_view(), name='Clean'),
    url(r'^employee/$', views.EmployeeViewSet.as_view(), name='Employee'),
    url(r'^booking/$', views.BookingViewSet.as_view(), name='Booking'),
]
