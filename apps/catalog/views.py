from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Catalog, Product
from django.db.models import Count

class CataloglistView(ListView):
    model = Catalog
    template_name = 'catalog/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = context['categories']
        products = Product.objects.filter(productcategory__category__in=categories)
        context['category_count'] = len(categories) if categories else 0
        context['product_count'] = len(products) if products else 0
        return context

    def get_queryset(self):
        return Catalog.objects.filter(parent=None)

class ProductByCategoryView(ListView):
    model = Catalog
    template_name = 'catalog/product_by_category.html'
    context_object_name = 'category'

    def get_queryset(self):
        self.category = Catalog.objects.get(slug=self.kwargs['slug'])
        self.categories = Catalog.objects.filter(parent=self.category)
        self.all_categories = self.categories.get_descendants(include_self=True)
        print(self.all_categories)
        queryset = Product.objects.filter(productcategory__category__in=self.all_categories)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.categories
        context['category'] = self.category
        context['category_count'] = self.categories.count()
        context['product_count'] = self.get_queryset().count()
        return context
        
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'