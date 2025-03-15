from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, ProductImage, Promotion

admin.site.register(Promotion)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    if Category.parent:
        list_display = ('pk', 'name', 'parent')
    else:
        list_display = ('pk', 'name', 'image')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, category):
        return mark_safe(f'<img src="{category.image.url}" width="100">')


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'quantity', 'get_image')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

    def get_image(self, product):
        images = product.images.all()
        if images:
            return mark_safe(f'<img src="{images[0].image.url}" width="150">')
        return 'salom'

