from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallary
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGallaryInline(admin.TabularInline):
    model = ProductGallary
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}
    inlines = [ProductGallaryInline]

class Variationadmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable = ('is_active',)   
    list_filter = ('product','variation_category','variation_value',)
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, Variationadmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallary)

