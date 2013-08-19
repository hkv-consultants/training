from django.db import models


class Location(models.Model):
	"""
	This class represents a location
	"""

	name = models.CharField(max_length=64)
	lat = models.DecimalField(max_digits=10, decimal_places=6)
	lon = models.DecimalField(max_digits=10, decimal_places=6)

	def __unicode__(self):
		return self.name


class RecordValueList(models.Model):
	"""
	List RecordValues for a specific location.
	This is referred to by RecordValue
	"""

	location = models.ForeignKey(Location)

	def __unicode__(self):
		return unicode(self.location)


class RecordValue(models.Model):
	"""
	This class represents a time labelled single record
	"""

	list = models.ForeignKey(RecordValueList)
	datetime = models.DateTimeField()
	value = models.FloatField()

	def __unicode__(self):
		return "%s, %s: %f" % (self.list, self.datetime, self.value)

