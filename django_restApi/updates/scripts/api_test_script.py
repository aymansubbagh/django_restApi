import requests
import json
BASE_URL 	= 'http://127.0.0.1:8000/'

BASE_URLs	= ['',
				'/json/update_model_detail_view',
				'/json/JsonCBV_get',
				'/json/JsonCBV2_get',
				'/json/userSerialize_serialize_get_all',
				'/json/userSerialize_serialize_get_user/user_id',
				'/json/Without',
				'/json/Without2',
				]

ENDPOINT	= 'api/'

ENDPOINT_URLs	= ['',
				'json/UpdateModelAPIView/',
				'json/UpdateModelListAPIView',
				]

def get_site_urls():
	r = requests.get(BASE_URL + ENDPOINT + ENDPOINT_URLs[1] + '2')
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		#print(type(r.json()))
		return r.json()
	return r.text

def create_update():
	new_data = {
			'user': 1,
			'content':	'Yet another new cool update',
	}
	#print(BASE_URL + ENDPOINT + ENDPOINT_URLs[1]+'1')
	r = requests.post(BASE_URL + ENDPOINT + ENDPOINT_URLs[2], data=json.dumps(new_data))
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		#print(r.json())
		return r.json()
	return r.text


print(create_update())
