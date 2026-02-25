# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for ViewSets
router = DefaultRouter()
router.register('patients', views.PatientViewSet)
router.register('doctors', views.DoctorViewSet)
router.register('appointments', views.AppointmentViewSet)

# urlpatterns must be defined!
urlpatterns = [
    # Include all router-generated URLs
    path('', include(router.urls)),
]