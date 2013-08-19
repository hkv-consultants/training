from django.db import models


class Location(models.Model):
	"""
	This class represents a location
	"""
	
	lat = models.DecimalField(max_digits=10, decimal_places=6)
	lon = models.DecimalField(max_digits=10, decimal_places=6)
	name = models.CharField(max_length=64)
	
	def __unicode__(self):
		return self.name
	