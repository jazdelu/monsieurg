#coding:utf8
from django import forms
from django.forms import ModelForm
from product.models import Product_Image



class ProductImageAdminForm(ModelForm):

	class Meta:
		model = Product_Image

	class Media:
		js = ('/static/js/admin_extra.js',)