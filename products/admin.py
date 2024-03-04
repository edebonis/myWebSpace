from django.contrib import admin
from .models import Products
from django.utils.html import format_html


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_image')

    def show_image(self, obj):
        print(obj.photo.url)
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))


admin.site.register(Products, ProductAdmin)
