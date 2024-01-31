# serializers.py
from rest_framework import serializers
from .models import HealthCenter, Clinician, Patient, PhysicalCheckup, Procedure, Medication, Illness, Symptom, Diagnose

class HealthCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCenter
        fields = '__all__'

class ClinicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinician
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PhysicalCheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalCheckup
        fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class IllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illness
        fields = '__all__'

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'

class DiagnoseSerializer(serializers.ModelSerializer):
    symptoms = SymptomSerializer(many=True, read_only=True)

    class Meta:
        model = Diagnose
        fields = '__all__'
