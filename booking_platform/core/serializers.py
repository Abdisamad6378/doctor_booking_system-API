from rest_framework import serializers
from .models import Patient , Doctor , Appointment

class Patientserializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class Doctorserializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class Appointmentserializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'