import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from .models import RFQ

@admin.action(description="Export Selected RFQs to CSV")
def export_rfqs_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stellar_shipers_rfqs.csv"'
    writer = csv.writer(response)
    writer.writerow([
        'Reference ID', 'Status', 'Date', 'Company', 'Contact Name', 'Email',
        'Phone', 'Country', 'Product', 'Quantity', 'Application', 'Packaging',
        'Destination', 'Incoterms', 'Sample Requested', 'Technical Requirements', 'Notes'
    ])
    for obj in queryset:
        prod_name = obj.product.name if obj.product else (obj.product_interest or "Custom")
        writer.writerow([
            obj.reference_id,
            obj.get_status_display(),
            obj.created_at.strftime('%Y-%m-%d %H:%M'),
            obj.company,
            obj.name,
            obj.email,
            obj.phone,
            obj.country,
            prod_name,
            obj.quantity,
            obj.application,
            obj.packaging,
            obj.delivery_country,
            obj.get_incoterms_display(),
            'YES' if obj.sample_request else 'NO',
            obj.technical_requirements,
            obj.message
        ])
    return response

@admin.action(description="Mark selected as REVIEWING")
def mark_reviewing(modeladmin, request, queryset):
    queryset.update(status='REVIEWING')

@admin.action(description="Mark selected as QUOTED")
def mark_quoted(modeladmin, request, queryset):
    queryset.update(status='QUOTED')

@admin.action(description="Mark selected as SAMPLE DISPATCHED")
def mark_sample(modeladmin, request, queryset):
    queryset.update(status='SAMPLE')


@admin.register(RFQ)
class RFQAdmin(admin.ModelAdmin):
    list_display = (
        'reference_id',
        'company',
        'name',
        'product_display',
        'quantity',
        'delivery_country',
        'sample_badge',
        'status',
        'created_at',
    )
    list_filter = ('status', 'sample_request', 'incoterms', 'created_at', 'delivery_country')
    search_fields = ('reference_id', 'company', 'name', 'email', 'delivery_country', 'product__name', 'product_interest')
    list_editable = ('status',)
    readonly_fields = ('reference_id', 'created_at', 'updated_at')
    actions = [export_rfqs_to_csv, mark_reviewing, mark_quoted, mark_sample]
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Inquiry Reference & Status', {
            'fields': (('reference_id', 'status'), 'created_at', 'updated_at')
        }),
        ('Buyer Enterprise Information', {
            'fields': (('company', 'name'), ('email', 'phone'), 'country')
        }),
        ('Sourcing Specifications & Application', {
            'fields': (
                ('product', 'product_interest'),
                ('quantity', 'application'),
                'technical_requirements',
                'technical_file',
                'sample_request',
            )
        }),
        ('Logistics & Packaging Preferences', {
            'fields': (
                ('packaging', 'delivery_country'),
                'incoterms',
                'message',
                'consent'
            )
        }),
        ('Internal CRM & Operations Desk', {
            'fields': ('admin_notes',),
            'classes': ('collapse',)
        }),
    )

    def product_display(self, obj):
        if obj.product:
            return obj.product.name
        return obj.product_interest or "Custom Sourcing"
    product_display.short_description = "Product"

    def sample_badge(self, obj):
        if obj.sample_request:
            return format_html('<span style="color:#10b981;font-weight:600;background:rgba(16,185,129,0.1);padding:2px 8px;border-radius:4px;border:1px solid #10b981;">SAMPLE REQ</span>')
        return format_html('<span style="color:#64748b;">Standard</span>')
    sample_badge.short_description = "Sample"
