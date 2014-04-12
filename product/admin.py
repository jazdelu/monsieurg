from django.contrib import admin
from product.models import Product, Product_Image

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display=('name','theme','origin',)
	fields =  ('name','theme','price','origin','description')
	list_filter = ('theme',)


class Product_Image_Admin(admin.ModelAdmin):
	readonly_fields=('image_tag',)
	list_display=('theme','product','position',)
	list_filter = ('theme','product',)
	fields = ('theme','product','image','image_tag','position',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Image, Product_Image_Admin )