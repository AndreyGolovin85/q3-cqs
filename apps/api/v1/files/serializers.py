
from rest_framework import serializers

from api.v1.reports.serializers import ReportSerializer
from files.models import CodeFile
from reports.models import Report


class CodeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeFile
        fields = '__all__'


class CodeFileRetrieveSerializer(serializers.ModelSerializer):
    checks = serializers.SerializerMethodField()
    last_check = serializers.SerializerMethodField()

    class Meta:
        model = CodeFile
        fields = ("uuid", "file", "last_check", "checks")

    def get_checks_report(self, obj):
        checks = Report.objects.filter(file=obj)
        return ReportSerializer(checks, many=True).data

    def get_last_check_report(self, obj):
        latest_report = Report.objects.filter(file=obj).order_by("-created").first()
        if latest_report:
            return latest_report.created
        return None
