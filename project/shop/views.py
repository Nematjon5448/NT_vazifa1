from django.urls import reverse_lazy

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Category, Comment


class IndexView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'shop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.filter(parent=None)
        return context

class SingleProduct(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/single-product.html'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments'] = Comment.objects.filter(product=self.object.pk)
        return context

class CommentSaqlash(CreateView):
    model = Comment
    template_name = 'shop/single-product.html'
    fields = ['text']
    pk_url_kwarg = 'product_id'

    def get_success_url(self):
        return reverse_lazy('single_product', kwargs={'product_id': self.object.product.pk})

    def form_valid(self, form):
        product_id = self.kwargs.get('product_id')
        form.instance.product = Product.objects.get(pk=product_id)
        form.instance.user = self.request.user
        return super().form_valid(form)
