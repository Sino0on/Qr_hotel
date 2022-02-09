from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from string import digits


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MenuIsDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['is_done']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    new_order = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_done = serializers.HiddenField(default=False)
    foods = FoodSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)
    # id = serializers.HiddenField(default=False)

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    new_order = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_done = serializers.HiddenField(default=False)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        foods = validated_data.pop('foods')
        food_ids = [i for i in foods]
        order = Order.objects.create(**validated_data)
        order.foods.add(*food_ids)
        return order

    def to_representation(self, instance):
        return OrderSerializer(instance).data


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room_number', 'qrcode', 'date_joined', 'is_staff', 'is_superuser', 'unhashed_password')


class RoomCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=4, min_length=4, read_only=True)
    unhashed_password = serializers.CharField(max_length=4, min_length=4, read_only=True)

    class Meta:
        model = Room
        fields = ('room_number', 'password', 'unhashed_password')

    def create(self, validated_data):
        return Room.objects.create_user(**validated_data)


