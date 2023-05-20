from django.urls import path
from . import views
from django.urls import path



urlpatterns = [
    path('csv_reader',views.csv_read ,name='csv_read'),
    path('api/csvdata/', views.CSVDataListCreateView.as_view(), name='csvdata-list'),
    path('api/csvdata/<int:pk>/', views.CSVDataRetrieveUpdateDestroyView.as_view(), name='csvdata-detail'),
    path('api/csvdata/export/', views.ExportFilteredCSVView.as_view(), name='csvdata-export'),
]
