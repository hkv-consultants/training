from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Location


def location_list(request):
    locations = Location.objects.all()

    context = {'locations':locations}
    return render_to_response('tijdreeksplot/location_list.html',
	                          context,
                          	  context_instance=RequestContext(request))