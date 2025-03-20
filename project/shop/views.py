from django.urls import reverse_lazy
from django.db.models import Max, Min, Sum, Avg
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Category, Comment, Promotion


class IndexView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'shop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.filter(parent=None)
        context['product_max_discount'] = Product.objects.all().order_by('-discount').first()
        context['promotion'] = Promotion.objects.last()
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

    def post(self, request, product_id=None):
        print(request.POST)
        return self.get(request, product_id)

class CommentSaqlash(CreateView):
    model = Comment
    template_name = 'shop/single-product.html'
    fields = ['text', 'rating']
    pk_url_kwarg = 'product_id'

    def get_success_url(self):
        return reverse_lazy('single_product', kwargs={'product_id': self.object.product.pk})

    def form_valid(self, form):
        product_id = self.kwargs.get('product_id')
        form.instance.product = Product.objects.get(pk=product_id)
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShopView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        slug = self.kwargs.get("category_slug")
        if self.request.method == 'POST':
            range_input = int(self.request.POST.get("rangeInput"))
            if slug:
                return Product.objects.filter(category__slug=slug, price__lte=range_input)
            return Product.objects.filter(price__lte=range_input)
        else:
            if slug:
                products = Product.objects.filter(category__slug=slug)
                return products
            return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()

        max_price =  self.get_queryset().aggregate(Max('price')).get("price__max")
        min_price =  self.get_queryset().aggregate(Min('price')).get("price__min")
        context['max_price'] = max_price
        context['min_price'] = min_price
        return context

    def post(self, request, category_slug=None):
        return self.get(request, category_slug)