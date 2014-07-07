from django.http import HttpResponse , Http404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import Context
from random import choice

def index(request):
	images = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 
	'image5.jpg']
	newimage = choice(images)
	context = Context({'image': newimage})
	return render(request, 'index.html', context)
	#return render_to_response('index.html')
	