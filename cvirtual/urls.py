from django.conf.urls import url, include
from django.contrib import admin
from main import urls as homeUrls
from blog import urls as blogUrls
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(homeUrls,namespace="main")),
    url(r'^blog/',include(blogUrls, namespace="blog")),
    #url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(regex=r'^media/(?P<path>.*)$',view=serve,kwargs={'document_root':settings.MEDIA_ROOT}),
]
