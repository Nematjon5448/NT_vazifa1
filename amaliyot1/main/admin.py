from django.contrib import admin
from .models import Rang, Brand, Car, Comment

# Register your models here.

admin.site.register(Rang)
admin.site.register(Brand)

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    readonly_fields = ['matni', 'foydalanuvchi']
    can_delete = False

class CarAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Car, CarAdmin)