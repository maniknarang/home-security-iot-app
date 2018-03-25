from django.shortcuts import render
from django.http import HttpResponse
import os
def index(request):
	# check which windows are open
	os.system('cd ..')
	win1 = os.path.isdir('win1')
	win2 = os.path.isdir('win2')
	print("Checking win1 : %s, win2: %s" % (win1, win2))
	d = {'win1' : win1, 'win2' : win2}
	return(render(request, 'list.html'))

# Create your views here.
