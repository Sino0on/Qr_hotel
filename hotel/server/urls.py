from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from knox.views import LoginView

from .views import *
from knox import views as knox_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('room/menu', OrderCreateView.as_view(), name='menu'),
    path('room/', RoomListView.as_view()),
    path('room/create/', RoomCreateView.as_view()),
    path('room/update-password/', RoomUpdatePassword.as_view()),
    path('room/login', LoginAPI.as_view()),
    path('foods/', FoodsView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('foods/is_done/<int:pk>', MenuIsDoneUpdateView.as_view()),
    path('food_add/', MenuCreateView.as_view()),
    path('food_update/<int:pk>', MenuUpdateView.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
    path('orders/', OrdersView.as_view())
    # path('auth_login/', LoginView.as_view())
    ]
