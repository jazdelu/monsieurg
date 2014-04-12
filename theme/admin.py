#coding:utf8
from django.contrib import admin
from theme.models import Theme, Preview_Image, Background_Image
from theme.forms import ThemeAdminForm
# Register your models here.

class Preview_Image_Admin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	list_display=('theme','image_tag',)
	fields = ('image','image_tag','theme',)

class Background_Image_Admin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	list_display = ('theme','image_tag','static')
	fields = ('image','image_tag','theme','static')

class ThemeAdmin(admin.ModelAdmin):
	list_display=('name','published','pub_date_format')
	form=ThemeAdminForm

	def pub_date_format(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")
	pub_date_format.admin_order_field = 'pub_date'
	pub_date_format.short_description = u'主题发布时间'

admin.site.register(Theme, ThemeAdmin)
admin.site.register(Preview_Image,Preview_Image_Admin)
admin.site.register(Background_Image,Background_Image_Admin)