from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # exclude = ('new_order',)

    def create(self, validated_data):
        print()
        return Order.objects.create(**validated_data)


class RoomSerializer(serializers.ModelSerializer):
    # qrcode = serializers.ImageField(source=)
    class Meta:
        model = Room
        fields = '__all__'


class RoomCreateSerializer(serializers.ModelSerializer):
    passwordnew = str(get_pin_code()).zfill(4)
    pin_code = serializers.HiddenField(default=passwordnew)
    password = serializers.HiddenField(default=make_password(passwordnew))


    class Meta:
        model = Room
        fields = ('room_number', 'password', 'pin_code')

