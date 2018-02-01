from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..models import Post
from .serializers import PostSerializer


class post_list(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

