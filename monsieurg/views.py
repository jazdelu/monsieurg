from django.shortcuts import render_to_response  
from django.template import RequestContext

def homepage(request):
	return render_to_response('index.html',{'slider':True},context_instance=RequestContext(request))

def ontheway(request):
	return render_to_response('ontheway.html',{},context_instance=RequestContext(request))

def story(request):
	return render_to_response('story.html',{'slider':False},context_instance=RequestContext(request))

def raise404(request):
	return render_to_response('404.html',{},context_instance=RequestContext(request))