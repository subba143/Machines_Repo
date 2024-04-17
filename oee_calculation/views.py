from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Machine, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer
#from .utils import calculate_oee, calculate_availability, calculate_performance, calculate_quality

#Create your views here.

class MachineListCreateAPIView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [IsAuthenticated]

class MachineRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [IsAuthenticated]

class ProductionLogListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer
    permission_classes = [IsAuthenticated]

class ProductionLogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer
    permission_classes = [IsAuthenticated]

# class OEEAPIView(generics.ListAPIView):
#     serializer_class = OeeSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         machine_id = self.request.query_params.get('machine_id')
#         start_date = self.request.query_params.get('start_date')
#         end_date = self.request.query_params.get('end_date')
#
#         # Filter production logs by machine and date range
#         queryset = ProductionLog.objects.filter(machine_id=machine_id, start_time__gte=start_date, end_time__lte=end_date)

        # Calculate OEE for each production log
        # oee_list = []
        # for production_log in queryset:
        #     availability = calculate_availability(production_log.machine.available_time, production_log.unplanned_downtime)
        #     performance = calculate_performance(production_log.ideal_cycle_time, production_log.actual_output, production_log.available_operating_time)
        #     quality = calculate_quality(production_log.good_product, production_log.total_product)
        #     oee = calculate_oee(availability, performance, quality)
        #     oee_list.append({
        #         'production_log_id': production_log.id,
        #         'oee': oee
        #     })
        #
        # return oee_list



