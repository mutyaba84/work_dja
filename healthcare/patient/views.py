from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import HealthCenter, Clinician, Patient, PhysicalCheckup, Procedure, Medication, Illness, Symptom, Diagnose
from .serializers import HealthCenterSerializer, ClinicianSerializer, PatientSerializer, PhysicalCheckupSerializer, ProcedureSerializer, MedicationSerializer, IllnessSerializer, SymptomSerializer, DiagnoseSerializer

class HealthCenterViewSet(viewsets.ModelViewSet):
    queryset = HealthCenter.objects.all()
    serializer_class = HealthCenterSerializer

class ClinicianViewSet(viewsets.ModelViewSet):
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PhysicalCheckupViewSet(viewsets.ModelViewSet):
    queryset = PhysicalCheckup.objects.all()
    serializer_class = PhysicalCheckupSerializer

class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class IllnessViewSet(viewsets.ModelViewSet):
    queryset = Illness.objects.all()
    serializer_class = IllnessSerializer

class SymptomList(generics.ListAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

class DiagnoseSearch(generics.ListAPIView):
    serializer_class = DiagnoseSerializer

    def get_queryset(self):
        symptoms_ids = self.request.query_params.getlist('symptoms', [])
        symptoms = Symptom.objects.filter(id__in=symptoms_ids)
        diagnoses = Diagnose.objects.filter(symptoms__in=symptoms).distinct()
        return diagnoses
