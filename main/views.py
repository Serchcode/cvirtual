from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class HomeView(View):
	"""docstring for Homeview"""
	def get(self, request):
		templatename = "home.html"
		return render (request,templatename)
		
	

