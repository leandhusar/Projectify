from rest_framework import serializers
from projectify.models.report import Report

class ReportSerializer(serializers.ModelSerializer):
    creation_date = serializers.SerializerMethodField()
    modification_date = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ("id", "project", "user", "percentage", "creation_date", "modification_date")

    def get_creation_date(self, obj):
        return obj.creation_date.isoformat()
    
    def get_modification_date(self, obj):
        return obj.modification_date.isoformat()
