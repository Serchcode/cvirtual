from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^', views.HomeView.as_view(), name='index'),
	url(r'^skills/', views.SkillsView.as_view(), name='skills'),
	url(r'^hobbies/', views.HobbieView.as_view(), name='hobbies'),
	url(r'^portfolio/', views.PortfolioView.as_view(), name='portfolio'),
	url(r'^curriculum/', views.CvView.as_view(), name='curriculum'),
	url(r'^contacto/', views.ContactView.as_view(), name='contacto'),
]