"""django_restApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from updates.views import *

urlpatterns = [
	path('', empty_url),
    path('admin/', admin.site.urls),
	path('json/update_model_detail_view', update_model_detail_view),
	path('json/JsonCBV_get', JsonCBV.as_view()),
	#path('json/JsonResponseMixin_render_to_json_response', JsonResponseMixin.render_to_json_response),
	path('json/JsonCBV2_get', JsonCBV2.as_view()),
	path('json/userSerialize_serialize_get_all', get_all),
	path('json/userSerialize_serialize_get_user/<int:pk>', get_user),
	path('json/Without', WithOut.as_view()),
	path('json/Without2', WithOut2.as_view()),
	path('api/', include('updates.api.urls')),
	
]



