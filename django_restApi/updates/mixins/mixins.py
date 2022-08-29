from django.http import HttpResponse
from ..api.utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class HttpResponseMixin(object):
	
	is_json = False
	@method_decorator(csrf_exempt)
	def render_to_response(self, data, status=200):
		content_type = 'text/html'
		if self.is_json:
			content_type = 'application/json'
		return HttpResponse(data,  content_type=content_type, status=status)
	