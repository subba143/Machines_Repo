from rest_framework import serializers
from .models import Machine, ProductionLog

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'machine_name', 'machine_serial_no', 'time']

class ProductionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLog
        fields = ['id', 'machine', 'cycle_no', 'unique_id', 'material_name', 'start_time', 'end_time', 'duration']

# class OeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductionLog
#         fields = ['production_log_id', 'oee']
