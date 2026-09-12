from django.contrib import admin
from .models import FAQ, PageContent

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'display_order', 'is_active', 'updated_at')
    list_filter = ('category', 'is_active')
    search_fields = ('question', 'answer')
    list_editable = ('display_order', 'is_active')

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'title', 'last_updated')
    search_fields = ('key', 'title', 'content')
