from django.contrib import admin
from .models import SiaSoType
from .models import PaymentStage
from .models import ExclusionPackage
from .models import SlabLevel
from .models import BearerPCR
from .models import PEORates
from .models import BBPackagePCR


admin.site.register(SiaSoType)
admin.site.register(PaymentStage)
admin.site.register(ExclusionPackage)
admin.site.register(SlabLevel)
admin.site.register(BearerPCR)
admin.site.register(PEORates)
admin.site.register(BBPackagePCR)