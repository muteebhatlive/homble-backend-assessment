from django.core.management.base import BaseCommand
from products.models import Sku
from decimal import Decimal

class Command(BaseCommand):
    help = "Update the selling price fields for all existing Sku records"

    def handle(self, *args, **options):
        skus = Sku.objects.all()
        for sku in skus:
            sku.platform_commission = sku.selling_price * Decimal('0.25')  #Calculate platform_fee
            sku.cost_price = sku.selling_price - sku.platform_commission  #Calculate cost_price
            sku.save()
        
        self.stdout.write("Successfully updated prices for Sku records")
