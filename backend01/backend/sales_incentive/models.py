from django.db import models

class SiaSoType(models.Model):
    product = models.CharField(max_length=50)
    sales_type = models.CharField(max_length=50)
    service_type = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    slab_eligibility = models.BooleanField()
    pcr_eligibility = models.BooleanField(db_column='PCR_ELI')
    created_date = models.DateField()
    created_user = models.CharField(max_length=50)
    updated_date = models.DateField(null=True, blank=True)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'sia_so_types'

    def __str__(self):
        return f"{self.product} - {self.sales_type}"
    
# PaymentStage is now a top-level class, not nested inside SiaSoType
class PaymentStage(models.Model):
    stage_id = models.CharField(max_length=50, primary_key=True)
    day_count = models.IntegerField()
    percentage = models.IntegerField()
    created_date = models.DateField()
    created_user = models.CharField(max_length=50)
    updated_date = models.DateField(null=True, blank=True)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'payment_stage'

    def __str__(self):
        return self.stage_id
    
class ExclusionPackage(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    tariff_id = models.CharField(max_length=50)
    tariff_name_pack = models.CharField(max_length=50)
    exclusion = models.BooleanField()
    created_date = models.DateField()
    created_user = models.CharField(max_length=50)
    updated_date = models.DateField(null=True, blank=True)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50)  # e.g., "ACTIVE", "INACTIVE"

    class Meta:
        db_table = 'exclusion_package'

    def __str__(self):
        return f"{self.tariff_name_pack} ({self.tariff_id})"
class SlabLevel(models.Model):
    id = models.AutoField(primary_key=True)
    slab_level = models.CharField(max_length=50)  # e.g., "1,2,3"
    upper_range = models.DecimalField(max_digits=15, decimal_places=2)
    lower_range = models.DecimalField(max_digits=15, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=50)
    updated_date = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=50)
    status = models.CharField(max_length=50)  # e.g., "ACTIVE", "INACTIVE"

    class Meta:
        db_table = 'slab_level'

    def __str__(self):
        return self.slab_level
    
class BearerPCR(models.Model):
    id = models.AutoField(primary_key=True)
    speed = models.CharField(max_length=50)
    service_order_type = models.CharField(max_length=50)
    with_bb_router = models.CharField(max_length=50, null=True, blank=True)
    without_bb_router = models.CharField(max_length=50, null=True, blank=True)
    tariff_id = models.CharField(max_length=50)
    tariff_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'bearer_pcr'

    def __str__(self):
        return f"{self.tariff_name} ({self.speed})"
    
class PEORates(models.Model):
    id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    tariff_id = models.CharField(max_length=50, null=True, blank=True)
    tariff_name = models.CharField(max_length=50, null=True, blank=True)
    pcr = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'peo_rates'

    def __str__(self):
        return f"{self.service_type} - {self.order_type}"
    
class BBPackagePCR(models.Model):
    id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    tariff_id = models.CharField(max_length=50, null=True, blank=True)
    tariff_name = models.CharField(max_length=50, null=True, blank=True)
    pcr = models.FloatField(null=True, blank=True)
    additional_cost = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'bb_package_pcr'

    def __str__(self):
        return f"{self.service_type} - {self.order_type}"
