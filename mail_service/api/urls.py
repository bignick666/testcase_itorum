from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, EntityViewSet


router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('entities', EntityViewSet, basename='entities')


urlpatterns = [
    path('api/', include(router.urls)),
]
