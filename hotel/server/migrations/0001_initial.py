# Generated by Django 4.0.2 on 2022-02-05 09:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('room_number', models.IntegerField(blank=True, unique=True, verbose_name='Номер комнаты')),
                ('pin_code', models.CharField(blank=True, max_length=4, verbose_name='Пин-код')),
                ('qrcode', models.ImageField(blank=True, upload_to='qr_codes/')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название блюда')),
                ('content', models.TextField(verbose_name='Описание блюда')),
                ('weight', models.IntegerField(verbose_name='Вес блюда')),
                ('image', models.ImageField(upload_to='dishes/')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наличии')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('order_date', models.DateTimeField(verbose_name='Время заказа')),
                ('is_done', models.BooleanField(default=False, verbose_name='')),
                ('new_order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='server.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='server.order')),
            ],
        ),
    ]
