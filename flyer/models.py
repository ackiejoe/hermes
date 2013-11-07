from django.db import models
from django.utils import timezone

# Create your models here.
# store: store,url,flyer_crawl,country,province,city,postalcode,insert,update
class Store(models.Model):
    store = models.CharField(max_length=50)
    url = models.CharField(max_length=200, blank=True)
    flyer_crawl = models.TextField(blank=True)
    insert = models.DateTimeField('inserted date', auto_now_add=True)
    update = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.store


#location: store,flyer_crawl,country,province,city,postal_code,insert,update
#self.store + ' ' + self.country + ' ' + self.city + ' ' + self.street + ' ' + self.postalcode
class Location(models.Model):
    store = models.ForeignKey(Store)
    flyer_crawl = models.TextField(blank=True)
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)
    insert = models.DateTimeField('inserted date', auto_now_add=True)
    update = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return unicode(self.store) + ' : ' + self.country + ' : ' + self.province + ' : ' + self.city + ' : ' + self.street + ' : ' + self.postalcode

#flyer: flyer,location,start_date,end_date,insert,update
class Flyer(models.Model):
    flyer = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    insert = models.DateTimeField('inserted date', auto_now_add=True)
    update = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.flyer
    def current_flyer(self):
        return self.start_date <= timezone.now() <= self.end_date
    current_flyer.admin_order_field = 'start_date'
    current_flyer.boolean = True
    current_flyer.short_description = 'Current Flyer?'

#product: product,insert,update
class Product(models.Model):
    product = models.CharField(max_length=50)
    insert = models.DateTimeField('inserted date', auto_now_add=True)
    update = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.product

#brand: brand,insert,update
class Brand(models.Model):
    brand = models.CharField(max_length=50)
    insert = models.DateTimeField('inserted date', auto_now_add=True)
    update = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.brand

#category: category,insert,update
class Category(models.Model):
    category = models.CharField(max_length=50)
    insert = models.DateTimeField('inserted date', auto_now_add=True)
    update = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.category

#sale: product,brand,category,flyer,price_sale,price_reg,unit,description,insert,update
class Sale(models.Model):
    product = models.ForeignKey(Product)
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey(Category)
    flyer = models.ForeignKey(Flyer)
    price_sale = models.IntegerField(default=0)
    price_reg = models.IntegerField(default=0, blank=True)
    unit = models.CharField(max_length=10, blank=True)
    description = models.TextField()
    insert_date = models.DateTimeField('inserted date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return unicode(self.product)

#saving: sale,saving,value,insert,update
class Saving(models.Model):
    sale = models.ForeignKey(Sale)
    value = models.IntegerField(default=0)
    saving = models.CharField(max_length=100)
    insert_date = models.DateTimeField('inserted date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    def __unicode__(self):
        return self.saving