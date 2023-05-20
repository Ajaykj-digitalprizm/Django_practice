from rest_framework import serializers
from .models import CSV_reader

class CSVDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV_reader
        fields = '__all__'
