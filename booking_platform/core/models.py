from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15 , unique=True)
    address = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='patient')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # In core/models.py - Patient model
    GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'), 
    ('Other', 'Other'),
]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    Full_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15 , unique=True)
    address = models.CharField(max_length=30)
    speciallization = models.CharField(max_length=30)
    Quallification = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=10 , unique=True)
    available_days = models.JSONField()
    slot_duration = models.IntegerField(default=30)
    available_time = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.Full_name} - {self.speciallization}"
    
    
class Appointment(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE , related_name="patient_profile")
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor_profile")
    STATUS_CHOICE = [
        ('Schedulled', 'Schedulled'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Pending', 'Pending'),
    ] 
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Schedulled')
    appointment_no = models.CharField(max_length=10,editable=False)
    appointment_time = models.TimeField()
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('appointment_time','appointment_no','Doctor')
    def __str__ (self):
        return f"Doctor: {self.Doctor.Full_name} - Patient: {self.Patient.name}"