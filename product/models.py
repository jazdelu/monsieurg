#coding:utf8
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from partner.models import Partner
from theme.models import Theme

GALLERY_POISTION_CHOICES=(
		('l',u'左栏'),
		('r',u'右栏'),
		('c',u'中心')
	)

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 128,verbose_name=u'产品名称')
	theme = models.ForeignKey(Theme,verbose_name=u'关联主题')
	price = models.CharField(max_length= 32,verbose_name=u'价格(¥)',blank=True)
	origin = models.CharField(max_length = 32, verbose_name=u'产地',blank=True)
	partner = models.ForeignKey(Partner,blank=True,null=True,verbose_name = u'供应商')
	description = models.TextField(blank=True,verbose_name = u'产品描述')
	pub_date = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name=u'礼盒单品'
		verbose_name_plural=u'礼盒单品'

	def __unicode__(self):
		return self.name

class Product_Image(models.Model):
	image = models.ImageField(upload_to='product/',verbose_name=u'上传图片')
	thumb_small = ImageSpecField(source='image',processors=[ResizeToFit(100)],format='JPEG',options={'quality': 80})
	thumb_middle = ImageSpecField(source='image',processors=[ResizeToFill(300,200)],format='JPEG',options={'quality': 80})
	thumb_big = ImageSpecField(source='image',processors=[ResizeToFill(600,400)],format='JPEG',options={'quality': 80})
	product = models.ForeignKey(Product,verbose_name='选择与此照片相关联的单品',blank=True,null = True,help_text = u'若为大图可不选')
	position = models.CharField(max_length=128,verbose_name=u'图片位置',choices=GALLERY_POISTION_CHOICES, blank=True)
	theme = models.ForeignKey(Theme,verbose_name = u'选择与此照片相关联的主题')
	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name=u'单品照片'
		verbose_name_plural=u'单品照片'
		ordering = ['theme','product','position']

	def __unicode__(self):
		return self.image.url

	def image_tag(self):
		return u'<img src="%s" />' % self.thumb_small.url
	image_tag.short_description = u'缩略图'
	image_tag.allow_tags = True







