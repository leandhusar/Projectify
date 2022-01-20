from django.contrib import admin
from services.models.project import Project
from services.models.report import Report

admin.site.register(Project)
admin.site.register(Report)
