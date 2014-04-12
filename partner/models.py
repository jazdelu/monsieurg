#coding:utf8
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
# Create your models here.
class Partner(models.Model):
	name = models.CharField(max_length=128,verbose_name=u'供应商名称')
	logo = models.ImageField(upload_to='logo/',verbose_name='Logo')
	thumb_small = ImageSpecField(source='image',processors=[ResizeToFit(100)],format='JPEG',options={'quality': 80})
	link = models.URLField(verbose_name=u'官方主页',blank = True, null = True)

	class Meta:
		verbose_name=u'供应商'
		verbose_name_plural=u'供应商'

	def __unicode__(self):
		return self.name

	def image_tag(self):
		return u'<img src="%s" />' % self.thumb_small.url
	image_tag.short_description = 'thumb'
	image_tag.allow_tags = True