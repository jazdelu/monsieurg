from django.shortcuts import render_to_response
from django.template import RequestContext
from theme.models import Theme,Preview_Image
from product.models import Product, Product_Image
from django.http import Http404
# Create your views here.
def review(request,tid):
	t = ''
	try:
		t = Theme.objects.get(id = int(tid))
	except:
		raise Http404
	l = Product_Image.objects.filter(theme=t).filter(position='l')
	c = Product_Image.objects.filter(theme=t).filter(position='c')
	r =  Product_Image.objects.filter(theme=t).filter(position='r')

	return render_to_response('review.html',{'l':l,'r':r, 'c':c, 't':t},context_instance=RequestContext(request))

def latest(request):
	try:
		pt = Theme.objects.get(published = True)
		t = Theme.objects.filter(published = False).filter(pub_date < pt.pub_date[0])
	except:
		raise Http404
	l = Product_Image.objects.filter(theme=t).filter(position='l')
	c = Product_Image.objects.filter(theme=t).filter(position='c')
	r =  Product_Image.objects.filter(theme=t).filter(position='r')

	return render_to_response('review.html',{'l':l,'r':r, 'c':c, 't':t},context_instance=RequestContext(request))