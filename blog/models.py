from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
	post_img = models.ImageField(upload_to='assets')
	post_title = models.CharField(max_length=100)
	post_content = models.TextField()
	post_date = models.DateTimeField()
	slug = models.SlugField()

	def get_absolute_url(self):
		return reverse('blog:detalle', args=[self.slug])


	def __str__(self):
		return self.post_title

