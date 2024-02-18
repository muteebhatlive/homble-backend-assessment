from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator


class Product(models.Model):
    """
    Very basic structure. To be further built up.
    """

    name = models.CharField(
        _("display name"),
        max_length=150,
        unique=True,
        help_text=_("This will be displayed to user as-is"),
    )
    # price = models.PositiveSmallIntegerField(
    #     _("selling price (Rs.)"),
    #     help_text=_("Price payable by customer (Rs.)"),
    # )
    description = models.TextField(
        _("descriptive write-up"),
        unique=True,
        help_text=_("Few sentences that showcase the appeal of the product"),
    )
    is_refrigerated = models.BooleanField(
        help_text=_("Whether the product needs to be refrigerated"),
        default=False,
    )
    category = models.ForeignKey(
        "categories.Category",
        related_name="products",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    managed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="managed_products",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    ingredients = models.CharField(
        _("ingredients"),
        max_length=500,
        default = 'Not Specified'
    )
    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        # Just to be explicit.
        db_table = "product"
        ordering = []
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Sku(models.Model):
    
    MEASUREMENT_UNIT_CHOICES = [
        ('gm', 'gm'),
        ('kg', 'kg'),
        ('ml', 'ml'),
        ('l', 'l'),
        ('pc', 'piece'),
    ]

    STATUS_CHOICES = [
        (0, 'Pending for approval'),
        (1, 'Approved'),
        (2, 'Discontinued'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField(validators=[MaxValueValidator(999)])
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    platform_commission = models.PositiveSmallIntegerField()
    cost_price = models.PositiveSmallIntegerField()
    measurement_unit = models.CharField(max_length=2, choices=MEASUREMENT_UNIT_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    markup_percentage = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)


    
    def save(self, *args, **kwargs):
        if self.cost_price:
            print(self.platform_commission)
            print(type(self.platform_commission))
            print(self.cost_price)
            print(type(self.cost_price))
            
            self.markup_percentage = (self.platform_commission / self.cost_price)
        self.selling_price = self.cost_price + self.platform_commission
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.product.name} - {self.size} gm"

    class Meta:
        unique_together = [['product', 'size']]