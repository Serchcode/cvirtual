from django.conf.urls import url, include
from django.contrib import admin
from main import urls as homeUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(homeUrls)),
]
