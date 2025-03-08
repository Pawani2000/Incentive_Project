from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiaSoTypeViewSet
from .views import PaymentStageViewSet
from .views import ExclusionPackageViewSet
from .views import SlabLevelViewSet
from .views import BearerPCRViewSet
from .views import PEORatesViewSet
from .views import BBPackagePCRViewSet

router = DefaultRouter()
router.register(r'sia-so-types', SiaSoTypeViewSet)
router.register(r'payment-stages', PaymentStageViewSet)
router.register(r'exclusion-packages', ExclusionPackageViewSet)
router.register(r'slab-levels', SlabLevelViewSet)
router.register(r'bearer-pcrs', BearerPCRViewSet)
router.register(r'peo-rates', PEORatesViewSet)
router.register(r'bb-package-pcrs', BBPackagePCRViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]