from rest_framework import serializers
from .models import SiaSoType
from .models import PaymentStage
from .models import ExclusionPackage
from .models import SlabLevel
from .models import BearerPCR
from .models import PEORates
from .models import BBPackagePCR

class SiaSoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiaSoType
        fields = '__all__'

class PaymentStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentStage
        fields = '__all__'

class ExclusionPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExclusionPackage
        fields = '__all__'

class SlabLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlabLevel
        fields = '__all__'

class BearerPCRSerializer(serializers.ModelSerializer):
    class Meta:
        model = BearerPCR
        fields = '__all__'

class PEORatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PEORates
        fields = '__all__'

class BBPackagePCRSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBPackagePCR
        fields = '__all__'