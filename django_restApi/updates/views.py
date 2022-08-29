from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
from django.views.generic import View
from updates.serialization.serialization import Serialize
#from updates.mixins.mixins import JsonResponseMixin

# Create your views here.

def empty_url(request):

	urls_dic = {
		'http://127.0.0.1:8000': ' "",'
		+' "/json/update_model_detail_view" ,'
		+' "/json/JsonCBV_get" ,'
		+' "/json/JsonCBV2_get" ,'
		+' "/json/userSerialize_serialize_get_all",'
		+' "/json/userSerialize_serialize_get_user/user_id",'
		+' "/json/Without", '
		+' "/json/Without2", ',
		
		'http://127.0.0.1:8000/api': ' "",'
		+' "/json/UpdateModelAPIView/user_id" ,'
		+' "/json/UpdateModelListAPIView" ,',
	}
	return JsonResponse(urls_dic)
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

	
def get_all(request, *args, **kwargs):
		
	return Serialize.serialize_1()
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

	
def get_user(request, pk):
		
	return Serialize.serialize_get_user(pk)
	
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------


def update_model_detail_view(request):
	import json
	data	=	{
		'first name':	'ayman',
		'last name':	'subbagh',
		'age':			'25',
		'location':		'update_model_detail_view',
	
	}
	json_data = json.dumps(data)
	
	return HttpResponse(json_data, content_type='application/json') # return json data
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------


class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data	=	{
			'first name':	'ayman',
			'last name':	'subbagh',
			'age':			'25',
			'location':		'JsonCBV.get',
		
		}
		
		return JsonResponse(data) # return json data
	
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

class JsonResponseMixin(object):
	
	def render_to_json_response(self, context, **response_kwargs):
		return JsonResponse(self.get_data(context), **response_kwargs) # return json data
	
	def get_data(self, context):
		return context


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

	
class JsonCBV2(JsonResponseMixin, View):
	
	def get(self, request, *args, **kwargs):
	
		data	=	{
			'first name':	'ayman',
			'last name':	'subbagh',
			'age':			'25',
			'location':		'JsonCBV2.get',
		
		}
		
		return self.render_to_json_response(data) # return json data
	
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

class WithOut(View):
	def get(request, *args, **kwargs):
		
		qs = Update.objects.all()
		json_data = Update.objects.all().serialize()
		return HttpResponse(json_data, content_type='application/json')
	
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------


class WithOut2(View):	
	def get(request, *args, **kwargs):
	
		obj = Update.objects.get(pk=1)
		json_data = obj.serialize()
		return HttpResponse(json_data, content_type='application/json')

