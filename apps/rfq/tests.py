from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from apps.rfq.models import RFQ
from apps.rfq.admin import export_rfqs_to_csv

class RFQAdminTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin_tester', 'admin_tester@stellarshipers.com', 'pass123!')
        self.client = Client()
        self.client.force_login(self.admin)
        self.rfq1 = RFQ.objects.create(
            reference_id='RFQ-2026-TEST1',
            name='Buyer One',
            company='Enterprise Alpha',
            country='Germany',
            email='buyer1@alpha.de',
            quantity='15 MT',
            application='Composite molding',
            delivery_country='Hamburg',
            sample_request=True,
            consent=True,
            status='NEW'
        )

    def test_admin_rfq_changelist_loads(self):
        url = reverse('admin:rfq_rfq_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enterprise Alpha')
        self.assertContains(response, 'RFQ-2026-TEST1')

    def test_admin_csv_export_action(self):
        url = reverse('admin:rfq_rfq_changelist')
        data = {
            'action': 'export_rfqs_to_csv',
            '_selected_action': [self.rfq1.pk],
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertIn('attachment; filename="stellar_shipers_rfqs.csv"', response['Content-Disposition'])
        content = response.content.decode('utf-8')
        self.assertIn('RFQ-2026-TEST1', content)
        self.assertIn('Enterprise Alpha', content)
        self.assertIn('buyer1@alpha.de', content)

    def test_admin_quick_status_action(self):
        url = reverse('admin:rfq_rfq_changelist')
        data = {
            'action': 'mark_reviewing',
            '_selected_action': [self.rfq1.pk],
        }
        response = self.client.post(url, data=data)
        self.rfq1.refresh_from_db()
        self.assertEqual(self.rfq1.status, 'REVIEWING')
