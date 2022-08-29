from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json


# Create your models here.
def upload_update_image(instance, filename):
	return f'updates/{instance.user}/{filename}'

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

class UpdateQuerySet(models.QuerySet):

	def serialize(self):
		qs = self
		final_array = []
		for obj in qs:
			struct = json.loads(obj.serialize())
			#print(struct)
			final_array.append(struct)
			#print(final_array)
		return json.dumps(final_array)


	#another approach for serializing list of json
	# def serialize(self):
		# running with the timestamp field will couse an error: datetime is not JSON serializable
		# list_values = list(self.values('user','content', 'image', 'timestamp'))

		# return json.dumps(list_values)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------


class UpdateManager(models.Manager):


	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self._db)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------


class Update(models.Model):
	user		=	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	content		=	models.TextField(blank=True, null=True)
	image		=	models.ImageField(upload_to=upload_update_image, blank=True, null=True)
	timestamp	=	models.DateTimeField(auto_now_add=True)

	objects = UpdateManager()


	def __str__(self):
		return self.content or ''

	def serialize(self):
		print(f'self -> {self}')
		'''
		Another approach
		json_data = serialize('json', [self], fields=('id', 'user','content', 'image'))
		json_dic = json.loads(json_data)
		json_dump = json.dumps(json_dic[0]['fields'])
		'''
		try:
			image = self.image.url
		except:
			image = ''
		data = {
			'id': self.id,
			'user': self.user.id,
			'content': self.content,
			'image': image
		}
		json_dump = json.dumps(data)
		return json_dump
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
