from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category


class IndexView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'shop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.filter(parent=None)
        return context

