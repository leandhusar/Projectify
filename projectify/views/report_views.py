from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from projectify.serializers.report_serializer import ReportSerializer
from projectify.models.report import Report

class ReportAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        report_set = Report.objects.filter(user=request.user)
        content = ReportSerializer(report_set, many=True).data
        return Response(content)
    
    def post(self , request):
        data = request.data
        data["user"] = request.user.id
        current_week = timezone.now().isocalendar()[1]
        report = Report.objects.filter(
            user = request.user, 
            project = request.data["project"]
        ).last()
        report_serializer = ReportSerializer(
            data = data
        )
        if report:
            last_report_week = report.creation_date.isocalendar()[1]
            is_valid = report_serializer.is_valid()
            if not last_report_week == current_week and is_valid:
                report_serializer.save()
                return Response(report_serializer.data)
            return Response(report_serializer.errors)
        else:
            is_valid = report_serializer.is_valid()
            if is_valid:
                report_serializer.save()
                return Response(report_serializer.data)
            return Response(report_serializer.errors)
    
    def put(self, request):
        current_month = timezone.now().month
        data = request.data
        data["user"] = request.user.id
        report = get_object_or_404(Report, pk=request.data["id"])
        data["project"] = report.project.id
        if report.creation_date.month != current_month:
            return Response(status=400)
        else:
            report_serializer = ReportSerializer(report, data=data)
            if report_serializer.is_valid():
                report_serializer.save()
                return Response(report_serializer.data)
            return Response(report_serializer.errors)
