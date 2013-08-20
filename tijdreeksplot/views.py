from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.template import RequestContext

from .models import Location, RecordValueList


def location_list(request):
    locations = Location.objects.all()

    context = {'locations':locations}
    return render_to_response('tijdreeksplot/location_list.html',
                              context,
                              context_instance=RequestContext(request))


class LocationDetail(DetailView):
    model = Location

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LocationDetail, self).get_context_data(**kwargs)
        location = context['object']
        context['record_values'] = RecordValueList.objects.filter(location = location)
        return context


class RecordValueListDetail(DetailView):
    model = RecordValueList

    def get_queryset(self):
        qs = super(RecordValueListDetail, self).get_queryset()
        self.location = get_object_or_404(Location, slug=self.kwargs['location_slug'])

        return qs.filter(location=self.location)

