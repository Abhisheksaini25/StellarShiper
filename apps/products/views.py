from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.filter(is_active=True).prefetch_related('images', 'documents')
        category_slug = self.request.GET.get('category')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        context['meta_title'] = 'Industrial Raw Materials & Export Catalog | STELLAR SHIPERS'
        context['meta_desc'] = 'Verified natural fibers, plant polymers, and agro-industrial biomass. Direct mill origin with certified lab testing and strict quality controls.'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Product.objects.filter(is_active=True).prefetch_related('images', 'documents')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context['primary_image'] = product.primary_image
        context['gallery_images'] = product.images.all()
        context['documents'] = product.documents.all()
        context['related_products'] = Product.objects.filter(is_active=True).exclude(id=product.id)[:3]
        context['meta_title'] = f'{product.name} - Technical Specifications & Export | STELLAR SHIPERS'
        context['meta_desc'] = f'Certified technical specifications for {product.name}. Laboratory tested parameters, extraction process, and B2B export terms.'
        return context
