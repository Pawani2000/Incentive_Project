from rest_framework import viewsets
from .models import SiaSoType
from .serializers import SiaSoTypeSerializer
from .models import PaymentStage
from .serializers import PaymentStageSerializer
from .models import ExclusionPackage
from .serializers import ExclusionPackageSerializer
from .models import SlabLevel
from .serializers import SlabLevelSerializer
from .models import BearerPCR
from .serializers import BearerPCRSerializer
from .models import PEORates
from .serializers import PEORatesSerializer
from .models import BBPackagePCR
from .serializers import BBPackagePCRSerializer

class SiaSoTypeViewSet(viewsets.ModelViewSet):
    queryset = SiaSoType.objects.all()
    serializer_class = SiaSoTypeSerializer

class PaymentStageViewSet(viewsets.ModelViewSet):
    queryset = PaymentStage.objects.all()
    serializer_class = PaymentStageSerializer

class ExclusionPackageViewSet(viewsets.ModelViewSet):
    queryset = ExclusionPackage.objects.all()
    serializer_class = ExclusionPackageSerializer

class SlabLevelViewSet(viewsets.ModelViewSet):
    queryset = SlabLevel.objects.all()
    serializer_class = SlabLevelSerializer

class BearerPCRViewSet(viewsets.ModelViewSet):
    queryset = BearerPCR.objects.all()
    serializer_class = BearerPCRSerializer

class PEORatesViewSet(viewsets.ModelViewSet):
    queryset = PEORates.objects.all()
    serializer_class = PEORatesSerializer

class BBPackagePCRViewSet(viewsets.ModelViewSet):
    queryset = BBPackagePCR.objects.all()
    serializer_class = BBPackagePCRSerializer