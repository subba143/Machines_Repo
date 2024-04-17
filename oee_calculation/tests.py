from django.test import TestCase
from .models import Machine, ProductionLog

# Create your tests here.

class MachineModelTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(machine_name='Machine 1', machine_serial_no='ABC123')

    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 1)
        self.assertEqual(str(self.machine), 'Machine 1')

class ProductionLogModelTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(machine_name='Machine 1', machine_serial_no='ABC123')
        self.production_log = ProductionLog.objects.create(machine=self.machine, cycle_no='CN001', unique_id='123456', material_name='Material 1', start_time='2024-04-01 08:00:00', end_time='2024-04-01 16:00:00', duration=8.0)

    def test_production_log_creation(self):
        self.assertEqual(ProductionLog.objects.count(), 1)
        self.assertEqual(str(self.production_log), 'Production Log - 123456')
