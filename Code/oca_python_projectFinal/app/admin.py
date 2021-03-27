from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    product = ('name', 'des', 'typeskin', 'time', 'image')