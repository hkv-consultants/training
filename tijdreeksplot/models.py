from django.db import models


class Location(models.Model):
    """
    This class represents a location
    """

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lon = models.DecimalField(max_digits=10, decimal_places=6)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('location-detail', (), {
            'slug': self.slug
        })


class RecordValueList(models.Model):
    """
    List RecordValues for a specific location.
    This is referred to by RecordValue
    """

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('recordvaluelist-detail', (), {
            'location_slug': self.location.slug,
            'slug': self.slug
        })


class RecordValue(models.Model):
    """
    This class represents a time labelled single record
    """

    value_list = models.ForeignKey(RecordValueList)
    datetime = models.DateTimeField()
    value = models.FloatField()

    def __unicode__(self):
        return "%s, %s: %f" % (self.value_list, self.datetime, self.value)

    class Meta:
        ordering = ['datetime']
