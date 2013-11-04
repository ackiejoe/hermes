from django.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=50)
    insert_date = models.DateTimeField('inserted date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.country
    
class Province_state(models.Model):
    country = models.ForeignKey(Country)
    Province_state = models.CharField(max_length=50)
    insert_date = models.DateTimeField('inserted date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.Province_state

class Store(models.Model):
    store = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    country = models.ForeignKey(Country)
    province_state = models.ForeignKey(Province_state)
    city = models.CharField(max_length=50)
    zip_postalcode = models.CharField(max_length=20)
    insert_date = models.DateTimeField('inserted date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.store
    
class Flyer(models.Model):
    flyer = models.CharField(max_length=200)
    store = models.ForeignKey(Store)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    insert_date = models.DateTimeField('inserted date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.flyer
    def current_flyer(self):
        return self.start_date <= timezone.now() <= self.end_date
    current_flyer.admin_order_field = 'start_date'
    current_flyer.boolean = True
    current_flyer.short_description = 'Current Flyer?'
    
class Product(models.Model):
    flyer = models.ForeignKey(Flyer)
    product = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    units = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    insert_date = models.DateTimeField('inserted date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.product
    
class Saving(models.Model):
    product = models.ForeignKey(Product)
    description = models.CharField(max_length=500)
    insert_date = models.DateTimeField('inserted date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.description