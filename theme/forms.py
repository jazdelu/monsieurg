#coding:utf8
from theme.models import Theme,Background_Image
from django.forms import ModelForm, ValidationError
from django.core.files.images import get_image_dimensions
class ThemeAdminForm(ModelForm):
	class Meta:
		model = Theme

	def clean_image(self):
		image = self.cleaned_data.get("image")
		if not image:
			raise ValidationError(u"请选择一张图片!")
		else:
			w, h = get_image_dimensions(image)
			if w < 1440:
				raise ValidationError(u"背景图片的宽度不能低于1440px!")

		return image


