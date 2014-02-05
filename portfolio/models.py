from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

# Create your models here.
class Block(models.Model):
	block_id = models.CharField(max_length=200)
	content = models.TextField()
	
	def __unicode__(self):
		return self.block_id
	
class Tag(models.Model):
	tag = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.tag
		
class Artwork(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	date_created = models.DateField(null=True, blank=True)
	artwork_tags = models.ManyToManyField(Tag)
	
	image = models.FileField(upload_to="artwork")
	image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(500, 500)], format='JPEG', options={'quality': 99})
	
	def __unicode__(self):
		return self.title