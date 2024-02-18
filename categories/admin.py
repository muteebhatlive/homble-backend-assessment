from django.contrib import admin

from categories.models import Category
from products.admin import ProductInline


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "products_count")
    ordering = ("id",)
    search_fields = ("name",)
    list_filter = ("is_active",)
    fields = ("id", "name","products_count", "is_active")
    # autocomplete_fields = ()
    readonly_fields = ("id","products_count")
    inlines = (ProductInline,)
