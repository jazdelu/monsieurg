from theme.models import Theme, Background_Image


def getPublishedThemeBackground(request):
	bg = ''
	bg_list = []
	try:
		t=Theme.objects.get(published=True)
		bg_list = Background_Image.objects.filter(theme = t)
		bg = Background_Image.objects.filter(theme = t).get(static = True)
	except:
		pass

	return {'bg_list':bg_list,'bg':bg}

def getReviewThemes(request):
	t=''
	try:
		t=Theme.objects.get(published=True)
	except:
		pass

	themes = Theme.objects.filter(published = False).filter(pub_date__lte =t.pub_date)
	return {'themes' : themes}