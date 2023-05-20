from django.contrib import admin
from .models import CSV_reader


# Register your models here.

class Csv_admin(admin.ModelAdmin):
    list_display=('Product_Family', 'Product_Code', 'Product_Description')
    list_display_links=('Product_Code',)
    list_filter = ('Product_Family',)  
    search_fields = ('Product_Family', 'Product_Code', 'Product_Description', 'Quantity_In_Stock', 'Available_Quantity', 'Allocated_Quantity', 'Price', 'Divider')  



admin.site.register(CSV_reader, Csv_admin)