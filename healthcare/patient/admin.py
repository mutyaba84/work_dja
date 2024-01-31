# admin.py
from django.contrib import admin
from .models import HealthCenter, Clinician, Patient, PhysicalCheckup, Procedure, Medication, Illness, Symptom, Diagnose

class PhysicalCheckupInline(admin.TabularInline):
    model = PhysicalCheckup
    extra = 1  # Number of inline forms to show

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender', 'nationality')
    search_fields = ('first_name', 'last_name', 'nationality')
    inlines = [PhysicalCheckupInline]

class ClinicianAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'title', 'license_number', 'email', 'health_center')
    search_fields = ('username', 'first_name', 'last_name', 'email')

class HealthCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'certification_number')
    search_fields = ('name', 'certification_number')

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'clinician_code')
    search_fields = ('name', 'clinician_code')

class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'clinician_code')
    search_fields = ('name', 'clinician_code')

class IllnessAdmin(admin.ModelAdmin):
    list_display = ('name', 'clinician_code')
    search_fields = ('name', 'clinician_code')

class SymptomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DiagnoseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name')
    filter_horizontal = ('symptoms',)

# Register your models with the custom admin classes
admin.site.register(HealthCenter, HealthCenterAdmin)
admin.site.register(Clinician, ClinicianAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PhysicalCheckup)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Illness, IllnessAdmin)
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Diagnose, DiagnoseAdmin)
