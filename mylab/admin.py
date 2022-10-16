from django.contrib import admin
from .models import *

admin.site.register(Prescription)

admin.site.register(Additives)

admin.site.register(Collectors)

admin.site.register(Medicals)

admin.site.register(Interval)

admin.site.register(Technique)

admin.site.register(Measurement)

admin.site.register(Doctor)

admin.site.register(Results)

admin.site.register(Settings)

class PatientAdmin(admin.ModelAdmin):
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        url ='templates/admin/prescription/?pks=' + ','.join(str([q.pk for q in queryset]))
       
    actions = [generatePDF]