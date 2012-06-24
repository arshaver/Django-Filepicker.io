from django.db import models

# Create your models here.

class FPImage(models.Model):
	"""(FPImage description)"""
	image = models.ImageField(upload_to='images')

	class Admin:
		list_display = ('image',)
		search_fields = ('',)

	def __unicode__(self):
		return u"FPImage"
