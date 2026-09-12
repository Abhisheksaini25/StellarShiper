tests_code = '''from django.test import TestCase, Client
from django.urls import reverse
from apps.products.models import Product, Category
from apps.rfq.models import RFQ

class StellarShiperHandoffComplianceTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Natural Plant Fibers', slug='natural-plant-fibers')
        self.product = Product.objects.create(
            category=self.category,
            name='Textile-grade raw banana fiber',
            slug='banana-fiber',
            raw_material='Musa plant pseudostems (G9 Grand Naine)',
            extraction_method='Mechanical decortication',
            processing='Drying only',
            harvest_origin='Jalgaon, Maharashtra, India',
            moq='500 kg',
            verified_specs={},
            provisional_specs={
                'Banana Variety': {'value': 'G9 (Grand Naine)', 'note': 'Supplier-stated'},
                'Extraction': {'value': 'Mechanical', 'note': 'Confirmed'}
            },
            is_active=True,
            is_featured=True
        )

    def test_all_10_core_pages_http_200(self):
        pages = [
            ('pages:home', {}),
            ('pages:about', {}),
            ('products:list', {}),
            ('products:detail', {'slug': self.product.slug}),
            ('pages:quality_process', {}),
            ('pages:services', {}),
            ('pages:contact', {}),
            ('pages:faq', {}),
            ('pages:privacy', {}),
            ('pages:terms', {}),
            ('pages:robots', {}),
        ]
        for url_name, kwargs in pages:
            url = reverse(url_name, kwargs=kwargs)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"Page {url} failed with status {response.status_code}")

    def test_homepage_handoff_content_and_positioning(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
        # Headline & supporting line (Page 3)
        self.assertContains(response, 'WHERE TRUST')
        self.assertContains(response, 'MEETS VALUE.')
        self.assertContains(response, 'Indian sourcing. International standards. Responsible export coordination.')
        # Origin & MOQ
        self.assertContains(response, 'Jalgaon, India')
        self.assertContains(response, '500 kg')
        # Brand pillars
        self.assertContains(response, 'Trust — Non-Negotiable')
        self.assertContains(response, 'Premium Value')
        self.assertContains(response, 'International Professionalism')
        # 6-Stage Process (Page 4)
        self.assertContains(response, 'Carefully selected sourcing network')
        self.assertContains(response, 'Requirement-led sourcing')
        self.assertContains(response, 'Quality verification before export')

    def test_specification_integrity_rules(self):
        response = self.client.get(reverse('products:detail', kwargs={'slug': self.product.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Textile-grade raw banana fiber')
        self.assertContains(response, 'Musa plant pseudostems')
        self.assertContains(response, 'Mechanical decortication')
        # Ensure notice about no generic internet values
        self.assertContains(response, 'No unverified number published')

    def test_rfq_submission_creates_record(self):
        data = {
            'name': 'Antoine Dubois',
            'company': 'Alsace Textile SA',
            'country': 'France',
            'email': 'a.dubois@alsacetextile.fr',
            'phone': '+33 3 88 12 34 56',
            'product': self.product.id,
            'quantity': '1000 kg trial lot',
            'application': 'Blended cotton-banana yarn development',
            'technical_requirements': 'Clean combed fiber bundles, 4-5 ft length',
            'packaging': 'Polythene export bags',
            'delivery_country': 'Port of Le Havre, France',
            'incoterms': 'CIF',
            'message': 'Sample evaluation lot needed for spinning trial.',
            'sample_request': True,
            'consent': True,
            'website_check': ''
        }
        response = self.client.post(reverse('rfq:submit'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('rfq:success'))
        
        rfq = RFQ.objects.filter(email='a.dubois@alsacetextile.fr').first()
        self.assertIsNotNone(rfq)
        self.assertTrue(rfq.sample_request)
        self.assertEqual(rfq.status, 'NEW')
'''

with open('apps/core/tests.py', 'w', encoding='utf-8') as f:
    f.write(tests_code)
print('apps/core/tests.py updated')
