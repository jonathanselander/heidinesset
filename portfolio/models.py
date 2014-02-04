from django.db import models

# Create your models here.
class Page(models.Model):
	page_id = models.CharField(max_length=200)
	content = models.TextField()
	
	def __unicode__(self):
		return self.page_id
	
class Tag(models.Model):
	tag = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.tag
		
class Artwork(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	date_created = models.DateField()
	image = models.FileField(upload_to="artwork")
	artwork_tags = models.ManyToManyField(Tag)
	
	def __unicode__(self):
		return self.title