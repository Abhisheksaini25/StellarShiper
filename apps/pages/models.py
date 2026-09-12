from django.db import models

class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('SOURCING', 'Direct Sourcing & Origin Verification'),
        ('SPECS', 'Technical Specifications & Lab Testing'),
        ('SAMPLES', 'Sample Dispatch & Evaluation Kits'),
        ('LOGISTICS', 'Shipping, Incoterms & Packaging'),
        ('COMMERCIAL', 'Payment Terms & Trade Contracts'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='SOURCING')
    question = models.CharField(max_length=300)
    answer = models.TextField(help_text="Detailed B2B answer. Supports HTML/paragraphs.")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['display_order', 'id']

    def __str__(self):
        return f"[{self.get_category_display()}] {self.question}"


class PageContent(models.Model):
    """
    CMS capability allowing admin to customize key page sections,
    hero taglines, mission statements, and corporate credentials.
    """
    SECTION_CHOICES = [
        ('HERO_SUBTITLE', 'Homepage Hero Subtitle'),
        ('ABOUT_MISSION', 'About Us - Core Mission Statement'),
        ('QUALITY_GUARANTEE', 'Quality & Process - Laboratory Verification Guarantee'),
        ('SOURCING_NETWORK', 'Sourcing Services - Direct Mill Network Summary'),
        ('CONTACT_NOTICE', 'Contact Desk - Commercial Notice'),
    ]

    key = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CMS Page Content Block"
        verbose_name_plural = "CMS Page Content Blocks"

    def __str__(self):
        return self.get_key_display()
