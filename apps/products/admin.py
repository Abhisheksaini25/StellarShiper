from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage, ProductDocument

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'caption', 'is_primary', 'display_order')

class ProductDocumentInline(admin.TabularInline):
    model = ProductDocument
    extra = 1
    fields = ('title', 'doc_type', 'document_file', 'file_size')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'raw_material', 'moq', 'is_featured', 'is_active', 'updated_at')
    list_filter = ('category', 'is_featured', 'is_active', 'created_at')
    search_fields = ('name', 'tagline', 'raw_material', 'hs_code', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductDocumentInline]

    fieldsets = (
        ('General Information', {
            'fields': (
                ('name', 'slug'),
                ('category', 'is_featured', 'is_active'),
                'tagline',
                'description',
                'applications',
            )
        }),
        ('Origin & Industrial Processing', {
            'fields': (
                ('raw_material', 'harvest_origin'),
                'extraction_method',
                'processing',
                'supplier_notes',
            )
        }),
        ('Specification Integrity (Verified vs Provisional)', {
            'description': 'CRITICAL REQUIREMENT: Do not present untested numbers as certified technical data. Partition verified laboratory parameters from supplier estimates.',
            'fields': (
                'verified_specs',
                'provisional_specs',
            )
        }),
        ('Commercial & Shipping Terms', {
            'fields': (
                ('moq', 'hs_code'),
                'packaging_details',
                'display_order',
            )
        }),
    )

@admin.register(ProductDocument)
class ProductDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'doc_type', 'file_size', 'created_at')
    list_filter = ('doc_type', 'created_at')
    search_fields = ('title', 'product__name')
