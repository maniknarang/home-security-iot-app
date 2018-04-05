from django.shortcuts import render
from django.http import HttpResponse
import os
from datetime import datetime
import winsound
import pygame

def index(request):
<<<<<<< HEAD
    return(render(request, 'list.html'))
=======
	f = open('log', 'a')
	s = ''
	if request.META['QUERY_STRING'] == 'lol':
		# DogSimulatorTM
		s += str(datetime.now()) + '\n'
		print(os.getcwd())
		winsound.PlaySound("dog.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
		
	print(s)
	f.write(s)
	f.close()
	f = open('log', 'r')
	
	log = []
	for line in f:
		log.append(line)
		
	# check which windows are open
	os.system('cd ..')
	win1 = os.path.isdir('win1')
	win2 = os.path.isdir('win2')
	w = [(win1, 0), (win2, 1)]
	print("Checking win1 : %s, win2: %s" % (win1, win2))
	log = log[::-1]
	f.close()
	return(render(request, 'list.html', {'windows' : w, 'log' : log[:10]}))
>>>>>>> b5d045c3a060970261dfdbec33936a5137cc90a7

# Create your views here.
