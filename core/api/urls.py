from rest_framework.routers import DefaultRouter
from django.urls import path,include
from landwind.urls import landwindRouter
router=DefaultRouter()
#posts
router.registry.extend(landwindRouter.registry)

urlpatterns=[
    path('',include(router.urls))
]