from django.contrib import admin
from flyer.models import Country
from flyer.models import Province_state
from flyer.models import Store
from flyer.models import Flyer
from flyer.models import Product
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
    
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['flyer', 'product', 'price', 'units', 'description']}),
    ]
    inlines = [SavingInline]
    list_display = ('product', 'price', 'units', 'description', 'flyer')

class ProductInline(admin.TabularInline):
    inlines = [SavingInline]
    model = Product
    extra = 5

class FlyerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['flyer', 'store']}),
        (None, {'fields': ['start_date', 'end_date']}),
    ]
    inlines = [ProductInline]
    list_display = ('flyer', 'current_flyer', 'store', 'start_date', 'end_date')

admin.site.register(Country)
admin.site.register(Province_state)
admin.site.register(Store)
admin.site.register(Flyer, FlyerAdmin)
admin.site.register(Product, ProductAdmin)
#admin.site.register(Saving)