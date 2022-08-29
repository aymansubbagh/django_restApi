from updates.models import Update
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from .mixin import CSRFExemptMixin
import json
from updates.mixins.mixins import HttpResponseMixin
from updates.forms import ModelUpdateForm
from .utils import is_json
def empty_url(request):





	urls_dic = {
		'site_urls': ' api/ ,'
		+'json/UpdateModelAPIView ,'
		+'json/UpdateModelListAPIView ,'
	}
	return JsonResponse(urls_dic)



class UpdateModelAPIView(HttpResponseMixin, CSRFExemptMixin, View):

	is_json = True

	def get_object(self, id=None):
		qs = Update.object.filter(id=id)
		if qs.count == 1:
			return qs.first()
		else:
			return None


	def get(self, request, pk, *args, **kwargs):
		obj = Update.objects.get(pk=pk)
		if obj is None:
			error_data = json.dumps({'message': 'user not found'})
			return self.render_to_response(error_data, status=404)
		json_data = obj.serialize()
		status_code = 200 # OK status
		return self.render_to_response(json_data, status_code)

	def post(self, request, *args, **kwargs):
		json_data = json.dumps({'message': 'Not Allowed, Please use the /api/ endpoints.'})
		status_code = 403 #Bad Request Status, 201 for Created Status
		return self.render_to_response(json_data, status_code)

	def put(self, request, pk, *args, **kwargs):
		valid_json = is_json(request.body)
		if not valid_json:
			error_data = json.dumps({'message': 'Invalid data sent, please send using JSON format.'})
			return self.render_to_response(error_data, status=400)

		obj = self.get_object(pk=pk)
		if obj is None:
			error_data = json.dumps({'message': 'Update not found'})
			return self.render_to_response(error_data, status=404)

		passed_data = json.loads(request.body)
		form = ModelUpdateForm(passed_data)
		if form.is_valid():
			obj = form.save(commit=True)
			obj_data = obj.serialize()
			return self.render_to_response(obj_data, status=201)
		if form.errors:
			data = json.dumps(form.errors)
			return self.render_to_response(data, status=400)



		json_data = json.dumps({'message': 'Something'})
		return self.render_to_response(json_data)

	def delete(self, request, id, *args, **kwargs):
		obj = self.get_object(id=id)
		if obj is None:
			error_data = json.dumps({'message': 'Update not found.'})
			return self.render_to_response(error_data, status=404)
		json_data = json.dumps({'message': 'Something'})
		return self.render_to_response(json_data, status=403)




class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):


	is_json = True

	def get(self, request, *args, **kwargs):
		qs = Update.objects.all()
		json_data = qs.serialize()
		status_code = 200 # OK status
		return self.render_to_response(json_data, status_code)


	def post(self, request, *args, **kwargs):
		valid_json = is_json(request.body)
		if not valid_json:
			error_data = json.dumps({'message': 'Invalid data sent, please send using JSON.'})
			return self.render_to_response(error_data, status=400)
		data = json.loads(request.body)
		form = ModelUpdateForm(data)
		if form.is_valid():
			obj = form.save(commit=True)
			obj_data = obj.serialize()
			return self.render_to_response(obj_data, status=201)
		if form.errors:
			data = json.dumps(form.errors)
			return self.render_to_response(data, status=400)
		json_data = json.dumps({'message': 'Not Allowed'})
		status_code = 400 #Bad Request Status, 201 for Created Status
		return self.render_to_response(json_data, status_code)


	# def put(self, request, *args, **kwargs):
		# json_data = json.dumps({'message': 'unknown data'})
		# status_code = 400 #Bad Request Status, 201 for Created Status
		# return self.render_to_response(json_data, status_code)

	def delete(self, request, *args, **kwargs):
		json_data = json.dumps({'message': 'can not delete an entire list.'})
		status_code = 403 #Forbidden Status
		return self.render_to_response(json_data, status_code)
