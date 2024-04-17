from django.urls import path
from .views import MachineListCreateAPIView, MachineRetrieveUpdateDestroyAPIView, ProductionLogListCreateAPIView, ProductionLogRetrieveUpdateDestroyAPIView

app_name = 'oee_calculation'

urlpatterns = [
    path('api/machines/', MachineListCreateAPIView.as_view(), name='machine-list-create'),
    path('api/machines/<int:pk>/', MachineRetrieveUpdateDestroyAPIView.as_view(), name='machine-detail'),
    path('api/production-logs/', ProductionLogListCreateAPIView.as_view(), name='production-log-list-create'),
    path('api/production-logs/<int:pk>/', ProductionLogRetrieveUpdateDestroyAPIView.as_view(), name='production-log-detail'),
 ]
