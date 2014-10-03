
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings


@csrf_exempt
def default_callback(request):

	token = getattr(settings, 'COGNALYS_REALTIME_API_TOKEN', '' )

	if request.POST and token != '':
		if request.POST.get('token') == token:


			
			

			return HttpResponse('', content_type="text/plain")

		else:

			return HttpResponse('Not Allowed', content_type="text/plain")



