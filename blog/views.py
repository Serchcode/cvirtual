from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Post

class ListView(View):
	def get(self, request):
		article = Post.objects.all()		
		template_name = 'blog_lista.html'
		context = {
		"article":article
		}
		return render(request,template_name,context)

class DetailView(View):
	def get(self,request,slug):
		template_name = 'blog_detalle.html'
		post = get_object_or_404(Post,slug=slug)
		context = {
		'post':post,
		}
		return render(request,template_name,context)