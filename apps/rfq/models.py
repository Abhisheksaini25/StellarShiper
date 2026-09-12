import uuid
from django.db import models
from apps.products.models import Product

class RFQ(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('REVIEWING', 'Reviewing'),
        ('QUOTED', 'Quoted'),
        ('SAMPLE', 'Sample Dispatched'),
        ('NEGOTIATION', 'Negotiation'),
        ('WON', 'Won / Order Confirmed'),
        ('LOST', 'Lost / Closed'),
    ]

    INCOTERM_CHOICES = [
        ('FOB', 'FOB (Free on Board)'),
        ('CIF', 'CIF (Cost, Insurance & Freight)'),
        ('CFR', 'CFR (Cost & Freight)'),
        ('EXW', 'EXW (Ex Works)'),
        ('FCA', 'FCA (Free Carrier)'),
        ('DDP', 'DDP (Delivered Duty Paid)'),
    ]

    # Reference tracking
    reference_id = models.CharField(max_length=30, unique=True, editable=False, db_index=True)

    # Buyer Contact Details
    name = models.CharField(max_length=150, verbose_name="Full Name / Representative")
    company = models.CharField(max_length=200, verbose_name="Company / Enterprise Legal Name")
    country = models.CharField(max_length=100, verbose_name="Buyer Country")
    email = models.EmailField(verbose_name="Official Corporate Email")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Phone / WhatsApp (Optional)")

    # Sourcing & Technical Specification
    product = models.ForeignKey(
        Product,
        related_name='rfqs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Target Catalog Product"
    )
    product_interest = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Product or Custom Sourcing Interest"
    )
    quantity = models.CharField(
        max_length=150,
        verbose_name="Estimated Quantity & Volume",
        help_text="e.g., '15 Metric Tons / month' or '2 x 40ft HQ FCL'"
    )
    application = models.CharField(
        max_length=255,
        verbose_name="Intended Industrial Application",
        help_text="e.g., Automotive Composites, Bio-packaging, Technical Textiles, Pulp"
    )
    technical_requirements = models.TextField(
        blank=True,
        verbose_name="Technical & Quality Requirements",
        help_text="Specify required tensile strength, fiber length, moisture %, or lab protocols."
    )
    technical_file = models.FileField(
        upload_to='rfq/specifications/',
        blank=True,
        null=True,
        verbose_name="Technical Drawing / Specification Sheet (Optional)",
        help_text="Upload PDF, DOC, or image (Max 10MB)"
    )

    # Logistics & Delivery
    packaging = models.CharField(
        max_length=150,
        blank=True,
        default="Standard Compressed Bales",
        verbose_name="Preferred Packaging",
        help_text="e.g., Compressed Bales (100kg), Palletized, Custom Poly-woven"
    )
    delivery_country = models.CharField(
        max_length=100,
        verbose_name="Destination Country / Port of Discharge"
    )
    incoterms = models.CharField(
        max_length=20,
        choices=INCOTERM_CHOICES,
        default='CIF',
        verbose_name="Preferred Incoterms"
    )
    message = models.TextField(
        blank=True,
        verbose_name="Commercial Notes / Additional Instructions"
    )

    # Flags & Governance
    sample_request = models.BooleanField(
        default=False,
        verbose_name="Request Physical Sample Kit",
        help_text="Check if physical verification sample lot is required prior to commercial quotation."
    )
    consent = models.BooleanField(
        default=True,
        verbose_name="B2B Commercial Consent",
        help_text="I confirm this is an authentic commercial inquiry and agree to B2B processing terms."
    )

    # Internal CRM Status & Management
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='NEW',
        verbose_name="RFQ Pipeline Status"
    )
    admin_notes = models.TextField(
        blank=True,
        verbose_name="Internal Sourcing Notes",
        help_text="Internal notes: mill allocation, shipping line quotes, follow-up log"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "RFQ"
        verbose_name_plural = "RFQs"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.reference_id:
            # Generate clean reference like RFQ-2026-A8F2
            short_id = uuid.uuid4().hex[:6].upper()
            from django.utils import timezone
            year = timezone.now().year
            self.reference_id = f"RFQ-{year}-{short_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        prod = self.product.name if self.product else (self.product_interest or "General Sourcing")
        return f"[{self.reference_id}] {self.company} - {prod} ({self.get_status_display()})"
