from django.contrib import admin

from products.models import Product, Sku


class SkuAdmin(admin.ModelAdmin):
    list_display = ("product", "size", "selling_price","cost_price", "platform_commission")
    search_fields = ("product__name",)
    autocomplete_fields = ("product",)
    
    
    
class SkuInline(admin.StackedInline):
    model = Sku
    extra = 0
    autocomplete_fields = ("product",)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "managed_by")
    ordering = ("-id",)
    search_fields = ("name",)
    list_filter = ("is_refrigerated", "category")
    fields = (
        ("name",),
        ("category", "is_refrigerated"),
        "description",
        "ingredients",
        ("id", "created_at", "edited_at"),
        "managed_by",
        
    )
    autocomplete_fields = ("category", "managed_by")
    readonly_fields = ("id", "created_at", "edited_at")
    inlines = [SkuInline]

class ProductInline(admin.StackedInline):
    """
    For display in CategoryAdmin
    """

    model = Product
    extra = 0
    ordering = ("-id",)
    readonly_fields = ("name","is_refrigerated")
    fields = (readonly_fields,)
    show_change_link = True

admin.site.register(Sku, SkuAdmin)