from django.contrib import admin

from .models import Category, Product, Pump, Puffer, Fournisseur, Review, ServiceAddons
from .models import SingleMaterial, CompleteSet

from django.http import HttpResponseRedirect






class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', "img", 'admin_photo',)
    list_filter = ('category',)
    search_fields = ('name',)

class PumpAdmin(admin.ModelAdmin):
    list_display = ("model", "description",
                    "power", "COP", "price", "date", "img", 'admin_photo',)
    list_filter = ("price",)
    prepopulated_fields = {"slug": ("model",)}
    


class PufferAdmin(admin.ModelAdmin):
    list_display = ("model", "capacity", "description",
                    "date", "img", "price", 'admin_photo' )
    list_filter = ("price",)
    prepopulated_fields = {"slug": ("model",)}


class FournisseurAdmin (admin.ModelAdmin):
    list_display = ("name", "street", "postal_code",
                    "city", "country", "phone",)


class SingleMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "date", "img", "price", 'admin_photo' )
    prepopulated_fields = {"slug": ("name",)}


class CompleteSetAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "date", "img", "price", 'admin_photo' )
    prepopulated_fields = {"slug": ("name",)}


class ServiceAddonsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "date", "img", "price", 'admin_photo' )
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

admin.site.register(Pump, PumpAdmin)
admin.site.register(Puffer, PufferAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)

admin.site.register(SingleMaterial, SingleMaterialAdmin)
admin.site.register(CompleteSet, CompleteSetAdmin)
admin.site.register(ServiceAddons, ServiceAddonsAdmin)

admin.site.register(Review)
