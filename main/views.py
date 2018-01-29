from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from wsgiref.util import FileWrapper
import requests
import json

class HomeView(View):
	"""docstring for Homeview"""
	def get(self, request):
		templatename = "index.html"
		return render (request,templatename)

class SkillsView(View):
	"""docstring for skillsView"""
	def get(self, request):
		templatename = "skills.html"
		return render (request,templatename)

class HobbieView(View):
	"""docstring for HobbieView"""
	def get(self, request):
		templatename = "hobbies.html"
		return render (request,templatename)

class PortfolioView(View):
	def get(self, request):
		templatename= "portafolio.html"
		response = requests.get('https://api.github.com/users/Serchcode/repos')
		repos = response.json()
		data_string = json.dumps(repos)
		decoded = json.loads(data_string)
		urls = [x['html_url'] for x in decoded]
		context = {
		'urls':urls,
		}
		return render(request,templatename,context)

class CvView(View):
	def get(self,request):
		templatename = "cv.html"
		return render(request,templatename)

class ContactView(View):
	def get(self,request):
		templatename = "contacto.html"
		return render(request,templatename)



