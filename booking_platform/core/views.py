from django.shortcuts import render
from.models import Patient, Doctor , Appointment
from.serializers import Patientserializer , Doctorserializer , Appointmentserializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = Patientserializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['phone','created_at']
    search_fields = ['name', 'phone']
    ordering_fields = ['created_at','name']
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = Doctorserializer
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = Appointmentserializer