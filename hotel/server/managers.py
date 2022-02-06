import random

from django.contrib.auth.base_user import BaseUserManager


def get_pin_code():
    pin_code = random.randint(1000, 9999)
    # while Room.objects.filter(pin_code=pin_code):
    #     pin_code = random.randint(1000, 9999)
    return pin_code


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, room_number, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not room_number:
            raise ValueError('The room_number must be set')
        room_number = room_number
        user = self.model(room_number=room_number, **extra_fields)
        passwordnew = str(get_pin_code()).zfill(4)
        print(passwordnew)
        user.set_password(passwordnew)
        user.save()
        return user

    def create_superuser(self, room_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        passwordnew = str(get_pin_code()).zfill(4)
        print(passwordnew)
        return self.create_user(room_number, password=passwordnew, **extra_fields)
