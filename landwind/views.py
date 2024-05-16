from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Package
from .serializers import PackageSerializer
class PackageViewSet(ModelViewSet):
    queryset=Package.objects.all()
    serializer_class=PackageSerializer
