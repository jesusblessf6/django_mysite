from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello World")

def detail(request, poll_id):
	return HttpResponse("You are looking at poll %s." % poll_id)

def results(request, poll_id):
	return HttpResponse("You are looking at results of poll %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("You are voting on poll %s" % poll_id)