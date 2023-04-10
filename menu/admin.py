from django.contrib import admin
from .models import FoodItem, Category
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['category_name']}
    list_display = ('category_name', 'vendor', 'updated_at')
    search_fields = ('category_name', 'vendor__vendor_name')



class FoodItemAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 50%" />'.format(object.image.url))
    
    thumbnail.short_description = 'Food Image'


    prepopulated_fields = {'slug': ['food_title']}
    list_display = ('thumbnail', 'food_title', 'vendor', 'category', 'price', 'is_available', 'updated_at')
    search_fields = ('food_title', 'vendor__vendor_name', 'price', 'category__category_name'),
    list_display_links = ('thumbnail', 'food_title')
    list_filter = ['is_available']



admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodItem, FoodItemAdmin)