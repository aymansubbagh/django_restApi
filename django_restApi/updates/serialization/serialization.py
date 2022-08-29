from django.views.generic import View
from updates.models import Update
from django.core.serializers import serialize
from django.http import HttpResponse
import json

class Serialize(View):
	def serialize_1(*args, **kwargs):

		qs = Update.objects.all()
		data = serialize('json', qs, fields=('user','content', 'image', 'timestamp'))
		#json_data = Update.objects.all().serialize()
		print(data)

		return HttpResponse(data, content_type='application/json')

	def serialize_get_user(pk):

		obj = Update.objects.get(pk=pk)
		data = serialize('json', [obj,], fields=('user','content', 'image', 'timestamp'))
		print(data)

		return HttpResponse(data, content_type='application/json')
