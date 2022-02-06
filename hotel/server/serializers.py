from django.contrib.auth import authenticate
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
    new_order = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = '__all__'
        # exclude = ('new_order',)

    def create(self, validated_data):
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


# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=4, min_length=4, read_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     class Meta:
#         model = Room
#         fields = ('room', 'password')
#
#     def create(self, validated_data):
#         return Room.objects.create_user(**validated_data)


# class LoginSerializer(serializers.Serializer):
#     password = serializers.CharField(max_length=4, write_only=True)
#
#     # Ignore these fields if they are included in the request.
#     room_number = serializers.CharField(max_length=255)
#     username = serializers.HiddenField(default=1)
#
#     def validate(self, data):
#         # self.context.get('request').parser_context.get('kwargs')  # your url parameter name here
#         # print(self.context)
#         room_number = data.get('room_number', None)
#         password = data.get('password', None)
#
#         # if room_number is None:
#         #     raise serializers.ValidationError(
#         #         'An room_number is required to log in.'
#         #     )
#
#         if password is None:
#             raise serializers.ValidationError(
#                 'A password is required to log in.'
#             )
#
#         room = authenticate(room_number=room_number, password=password)
#
#         if room is None:
#             raise serializers.ValidationError(
#                 'A room with this email and password was not found.'
#             )
#
#         if not room.is_active:
#             raise serializers.ValidationError(
#                 'This room has been deactivated.'
#             )
#
#         return data