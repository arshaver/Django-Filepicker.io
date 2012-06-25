from django.db import models

# Create your models here.

class FPImage(models.Model):
	"""(An image uploaded from Filepicker.io)"""
	image = models.ImageField(upload_to='images')

	class Meta:
		verbose_name = "filepicker.io image"
		
	def __unicode__(self):
		return u"%s" %str(self.image).split("/")[-1]
