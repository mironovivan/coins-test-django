from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

ROUTER = DefaultRouter()
ROUTER.register(r'accounts', views.AccountsViewSet)


urlpatterns = [
    path('', include(ROUTER.urls)),
]
