from django.shortcuts import render_to_response
from django.template import RequestContext
from theme.models import Theme,Preview_Image
from django.http import Http404

# Create your views here.
def order(request):
	l =[]
	try:
		t=Theme.objects.get(published =True)
		l = Preview_Image.objects.filter(theme=t)
	except Theme.DoesNotExist:
		raise Http404
	return render_to_response('order.html',{'preview_list':l,'slider':False,'pt':t},context_instance=RequestContext(request))
