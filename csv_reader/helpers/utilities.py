import csv
import os
from django.conf import settings
from ..models import CSV_reader


def csv_read_func(request):
    media_root = settings.MEDIA_ROOT
    file_path = os.path.join(media_root, 'Product.csv')
 
    # Read the CSV file and upload data to the database
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            CSV_reader.objects.create(Product_Family=row['Product Family'], Product_Code=row['Product Code'], Product_Description = row['Product Description'],
                                Quantity_In_Stock=row['Quantity In Stock'], Available_Quantity=row['Available Quantity'], Allocated_Quantity = row['Allocated Quantity'],
                                Price=row['Price'], Divider=row['Divider'])
    
    return