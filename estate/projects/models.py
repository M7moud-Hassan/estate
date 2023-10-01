from django.db import models

from engineers.models import Engineers
from imported.models import Imported


class Projects(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    date_session = models.DateField(null=True, blank=True)
    date_finance = models.DateField(null=True, blank=True)
    date_notification_Altrsih = models.DateField(null=True, blank=True)
    date_sadad_khatab_alkhsmat = models.DateField(null=True, blank=True)
    date_asnad = models.DateField(null=True, blank=True)
    date_work = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    date_extra_end = models.IntegerField(default=0)
    duration_project = models.IntegerField(null=True, blank=True)
    price_project = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gramat_altakheer = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_price_end = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    insurance_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ahdaa = models.ManyToManyField('Ahdaa', blank=True)
    masourfats = models.ManyToManyField('Masourfat', blank=True)
    mostakhlas = models.ManyToManyField('Mostakhlas', blank=True)
    durations=models.ManyToManyField('AdditionalPeriods', blank=True)
    report=models.TextField(null=True)


class Ahdaa(models.Model):
    engineer_id = models.ForeignKey(Engineers, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Masourfat(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_masrouf = models.DateField(null=True, blank=True)
    imported = models.ForeignKey(Imported, on_delete=models.CASCADE, null=True, blank=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    bain_masrouf = models.ForeignKey(Engineers, on_delete=models.CASCADE, null=True, blank=True)

class AdditionalPeriods(models.Model):
    price_increase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_Period = models.DateField(null=True, blank=True)
    terminationBeforeTheIncrease = models.DateField(null=True, blank=True)
    terminationAfterTheIncrease = models.DateField(null=True, blank=True)
    reason = models.CharField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=500, null=True, blank=True)
    


class Mostakhlas(models.Model):
    engineer_id= models.ForeignKey(Engineers, on_delete=models.CASCADE, null=True, blank=True)
    date_mostakhlas = models.DateField(null=True, blank=True)
    workforce = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Combined_discount_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bank_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    engineering_stamp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    others = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_mostakhlas_after = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    actual_extract_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    altaminat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_deductions_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_deductions_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    commercial_ndustrial_profits_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    value_added_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stamp_tax_division = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    martyrs_Honor_fund = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    resource_development_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    long_Live_egypt_fund = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    applied_tear = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    union_of_two_sayings = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.CharField(max_length=10000, null=True, blank=True)
