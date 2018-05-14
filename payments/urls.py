from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

ROUTER = DefaultRouter()
ROUTER.register(r'payments', views.PaymentsViewSet)


urlpatterns = [
    path('', include(ROUTER.urls)),
]
