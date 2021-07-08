from django.urls import path, include
from rest_framework.routers import DefaultRouter

from openmrs_viamo import views

router = DefaultRouter() 
router.register('visits', views.AppointmentViewSet, basename='visit')

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]