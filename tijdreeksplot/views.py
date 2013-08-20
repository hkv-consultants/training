from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.template import RequestContext

from .models import Location, RecordValueList


def location_list(request):
    locations = Location.objects.all()

    context = {'locations':locations}
    return render_to_response('tijdreeksplot/location_list.html',
                              context,
                              context_instance=RequestContext(request))

class RecordValueListList(ListView):
    model = RecordValueList

    def get_queryset(self):
        qs = super(RecordValueListList, self).get_queryset()
        self.location = get_object_or_404(Location, name=self.args[0])
        return qs.filter(location=self.location)