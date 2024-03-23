from django.shortcuts import render
from django.views.generic import ListView
from .models import Catalog, Product

class CataloglistView(ListView):
    model = Catalog
    template_name = 'catalog/index.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_count'] = Catalog.objects.count()
        context['product_count'] = Product.objects.count()
        return context
    