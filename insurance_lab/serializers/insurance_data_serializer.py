from rest_framework import serializers

from insurance_lab.models.insurance_data import InsuranceData


class InsuranceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceData
        fields = '__all__'
