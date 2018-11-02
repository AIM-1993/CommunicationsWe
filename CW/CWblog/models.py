from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Author(models.Model):
	objects = models.Manager()
	author = models.CharField(max_length=30)

	def __str__(self):
		return self.author


class Article(models.Model):
	objects = models.Manager()
	title = models.CharField(max_length=50)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	published = models.BooleanField(default=True)
	pub_date = models.DateTimeField("date_published")
	contents = RichTextField()

	def __str__(self):
		return self.title
