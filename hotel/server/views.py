from rest_framework.permissions import IsAdminUser

from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics


class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomCreateSerializer
    permission_classes = (IsAdminUser, )


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)

    # def get_queryset(self):
    #     if self.request.method == 'POST':
    #         return OrderCreateSerializer
    #     else:
    #         return OrderSerializer


class OrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
