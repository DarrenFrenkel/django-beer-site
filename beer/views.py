from django.shortcuts import render_to_response
from django.template import RequestContext
from beer.models import Beer

def BeersAll(request):
	beers = Beer.objects.all().order_by('name')
	context = {'beers': beers}
	return render_to_response('beersall.html', context, context_instance=RequestContext(request))

	

# Create your views here.
