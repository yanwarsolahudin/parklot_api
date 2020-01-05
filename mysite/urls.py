from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from floors.views import FloorViewSet
from parks.views import ParkViewSet
from payments.views import PaymentViewSet
from slots.views import SlotViewSet
from tickets.views import TicketViewSet
from users.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

# ViewSet Router
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'parks', ParkViewSet, basename='park')
router.register(r'floors', FloorViewSet, basename='floor')
router.register(r'slots', SlotViewSet, basename='slot')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns += router.urls
