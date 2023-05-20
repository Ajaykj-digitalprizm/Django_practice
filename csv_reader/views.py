import csv
from .models import CSV_reader
from django.http import HttpResponse
from .serializers import CSVDataSerializer
from rest_framework import generics, filters, renderers
from django_filters.rest_framework import DjangoFilterBackend
from .helpers.utilities import csv_read_func




def csv_read(request):

    res = csv_read_func

    if res:
        return HttpResponse('CSV data Uploaded successfully.')




# class CustomPagination(pagination.PageNumberPagination):
#     page_size = 10  # Set the number of instances to return per page
#     page_size_query_param = 'page_size'
#     max_page_size = 10


class CSVDataListCreateView(generics.ListCreateAPIView):
    queryset = CSV_reader.objects.all()
    serializer_class = CSVDataSerializer
    # pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['Product_Family']  # Add more fields for filtering
    search_fields = ['Product_Family', 'Product_Code','Product_Description'] 

    

class CSVDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CSV_reader.objects.all()
    serializer_class = CSVDataSerializer



class ExportFilteredCSVView(generics.ListAPIView):
    queryset = CSV_reader.objects.all()
    serializer_class = CSVDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['Product_Family']       # Add more fields for filtering
    search_fields = ['Product_Family']          # Add more fields for searching

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="filtered_data.csv"'

        writer = csv.writer(response)
        headers = ['Product_Family', 'Product_Code', 'Product_Description', 'Quantity_In_Stock', 'Available_Quantity', 'Allocated_Quantity']  # Add more fields for CSV headers
        writer.writerow(headers)

        for item in serializer.data:
            row = [item['Product_Family'], item['Product_Code'], item['Product_Description'], item['Quantity_In_Stock'], 
                item['Available_Quantity'], item['Allocated_Quantity'],  item['Price'], item['Divider']]
            writer.writerow(row)

        return response