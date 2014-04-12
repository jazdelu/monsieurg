from django.contrib import admin
from partner.models import Partner
# Register your models here.
class PartnerAdmin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	list_display = ('name','image_tag','link')
	fields = ('name','link','logo','image_tag')

admin.site.register(Partner,PartnerAdmin)