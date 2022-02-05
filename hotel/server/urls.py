from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('room/<int:pk>', OrderCreateView.as_view()),
    path('room/', OrdersView.as_view()),
    path('room/create/', RoomCreateView.as_view())
    ]
