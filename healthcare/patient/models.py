
from django.db import models
from django.contrib.auth.models import AbstractUser

class HealthCenter(models.Model):
    name = models.CharField(max_length=100)
    certification_number = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Clinician(AbstractUser):
    title = models.CharField(max_length=50)
    license_number = models.CharField(max_length=20, unique=True)
    health_center = models.ForeignKey(HealthCenter, on_delete=models.SET_NULL, null=True, blank=True)
    # Add other fields as needed

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name} ({self.username})"

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Add other fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PhysicalCheckup(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinician = models.ForeignKey(Clinician, on_delete=models.SET_NULL, null=True, blank=True)
    health_center = models.ForeignKey(HealthCenter, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    findings = models.TextField()

    def __str__(self):
        return f"Checkup for {self.patient} on {self.date}"

class Procedure(models.Model):
    name = models.CharField(max_length=100)
    clinician_code = models.CharField(max_length=10)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Medication(models.Model):
    name = models.CharField(max_length=100)
    clinician_code = models.CharField(max_length=10)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Illness(models.Model):
    name = models.CharField(max_length=100)
    clinician_code = models.CharField(max_length=10)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Diagnose(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom)

    def __str__(self):
        return self.name
