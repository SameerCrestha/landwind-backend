from rest_framework.routers import DefaultRouter
from .views import PackageViewSet
landwindRouter=DefaultRouter()
landwindRouter.register(r'packages',PackageViewSet)