from rest_framework.serializers import ModelSerializer
from .models import Package
class PackageSerializer(ModelSerializer):
    class Meta:
        model=Package
        exclude=['created_date','modified_date']