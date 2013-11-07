from django.contrib import admin
from flyer.models import Store
from flyer.models import Location
from flyer.models import Flyer
from flyer.models import Product
from flyer.models import Brand
from flyer.models import Category
from flyer.models import Sale
from flyer.models import Saving

# class CountryAdmin(admin.ModelAdmin):
#     fieldsets = [
#                  (None, {'fields': ['name']}),
#                  (None, {'fields': ['insert_date']}),
#                  (None, {'fields': ['update_date']}),
#     ]
#     list_display = ('name', 'insert_date', 'update_date')
#      
#      
# class Province_stateAdmin(admin.ModelAdmin):
#     fieldsets = [
#                  (None, {'fields': ['country']}),
#                  (None, {'fields': ['name']}),
#                  (None, {'fields': ['insert_date']}),
#                  (None, {'fields': ['update_date']}),
#     ]

class SavingInline(admin.TabularInline):
    model = Saving
    extra = 1
    
class SaleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product', 'brand', 'category', 'flyer', 'price_sale', 'price_reg', 'unit', 'description']}),
    ]
    inlines = [SavingInline]
    list_display = ('product', 'brand', 'category', 'flyer', 'price_sale', 'price_reg', 'unit', 'description')

class SaleInline(admin.TabularInline):
    model = Sale
    extra = 5

class FlyerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['flyer', 'location']}),
        (None, {'fields': ['start_date', 'end_date']}),
    ]
    inlines = [SaleInline]
    list_display = ('flyer', 'current_flyer', 'location', 'start_date', 'end_date')

admin.site.register(Store)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Flyer, FlyerAdmin)
admin.site.register(Sale, SaleAdmin)