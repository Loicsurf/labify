from django.contrib import admin
from .models import Prescription, Additives, Collectors, LabTechnician, Medicals, Interval, Technique, Measurement, Doctor

admin.site.register(Prescription)

admin.site.register(Additives)

admin.site.register(Collectors)

admin.site.register(LabTechnician)

admin.site.register(Medicals)

admin.site.register(Interval)

admin.site.register(Technique)

admin.site.register(Measurement)

admin.site.register(Doctor)