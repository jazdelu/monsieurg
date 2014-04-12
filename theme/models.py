#coding:utf8
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from datetime import *
# Create your models here.
def preview_path_handler(instance,filename):
	filename=datetime.now().strftime('%Y%m%d%H%M%S%f')
	return 'preview/{theme}/{file}'.format(theme=instance.theme.name,file=filename)

def background_path_handler(instance,filename):
	filename=datetime.now().strftime('%Y%m%d%H%M%S%f')
	return 'background/{theme}/{file}'.format(theme=instance.theme.name,file=filename)

class Theme(models.Model):
	name = models.CharField(max_length=128,verbose_name=u'主题名称')
	desciption = models.TextField(blank=True,verbose_name= '主题描述')
	deadline=models.DateField(verbose_name=u'寄送时间')
	pub_date=models.DateTimeField(auto_now_add = True, editable = False)
	published = models.BooleanField(verbose_name=u'是否发布该主题？',help_text=u'若勾选此项，之前发布的礼盒主题将会自动撤销发布.')

	class Meta:
		verbose_name='礼盒主题'
		verbose_name_plural=u'礼盒主题'
		ordering  = ['-pub_date',]

	def __unicode__(self):
		return self.name

	def save(self,*args, **kwargs):
		if self.published:
			try:
				t = Theme.objects.get(published = True)
				t.published = False
				l.save()
			except:
				pass
		else:
			try:
				t = Theme.objects.get(published = True)
			except:
				t = Theme.objects.filter(published = False)
				if t:
					t[0].published = True
					t[0].save()
				else:
					pass
		super(Theme, self).save(*args, **kwargs)


class Preview_Image(models.Model):
	name = models.CharField(max_length=128,verbose_name='图片名称',blank =True,null = True)
	image= models.ImageField(upload_to='preview/', verbose_name=u'上传图片',)
	thumb_small= ImageSpecField(source=u"image",processors=[ResizeToFit(100)],format="JPEG",options={"quality": 80})	
	thumb_middle= ImageSpecField(source=u"image",processors=[ResizeToFill(390,220)],format="JPEG",options={"quality": 80})	
	theme= models.ForeignKey(Theme,verbose_name=u'关联主题')
	pub_date=models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name=u'预览幻灯片'
		verbose_name_plural=u'预览幻灯片'

	def __unicode__(self):
		return self.image.url

	def image_tag(self):
		return u'<img src="%s" />' % self.thumb_small.url
	image_tag.short_description = u'缩略图'
	image_tag.allow_tags = True

class Background_Image(models.Model):
	name = models.CharField(max_length=128,verbose_name=u'图片名称',null = True,blank = True)
	image= models.ImageField(upload_to='background/', verbose_name=u'上传图片')
	thumb_small= ImageSpecField(source=u"image",processors=[ResizeToFit(100)],format="JPEG",options={"quality": 80})
	theme= models.ForeignKey(Theme,verbose_name=u'关联主题')
	static=models.BooleanField(verbose_name=u'是否设置为静态背景？',help_text = u'若勾选此项，之前发布的静态背景将会自动撤销发布.')
	pub_date=models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name=u'背景图'
		verbose_name_plural=u'背景图'

	def __unicode__(self):
		return self.image.url

	def image_tag(self):
		return u'<img src="%s" />' % self.thumb_small.url
	image_tag.short_description = u'缩略图'
	image_tag.allow_tags = True

	def save(self,*args, **kwargs):
		if self.static:
			try:
				b = Background_Image.objects.filter(theme = self.theme).get(static = True)
				b.static = False
				l.save()
			except:
				pass
		else:
			pass

		super(Background_Image, self).save(*args, **kwargs)
