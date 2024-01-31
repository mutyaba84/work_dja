"""
URL configuration for healthcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""  
# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import HealthCenterViewSet, ClinicianViewSet, PatientViewSet, PhysicalCheckupViewSet, ProcedureViewSet, MedicationViewSet, IllnessViewSet, SymptomList, DiagnoseSearch

router = routers.DefaultRouter()
router.register(r'health-centers', HealthCenterViewSet)
router.register(r'clinicians', ClinicianViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'physical-checkups', PhysicalCheckupViewSet)
router.register(r'procedures', ProcedureViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'illnesses', IllnessViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/symptoms/', SymptomList.as_view(), name='symptom-list'),
    path('api/diagnose/search/', DiagnoseSearch.as_view(), name='diagnose-search'),
]
