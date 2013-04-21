from django.conf.urls import patterns, url, include
from tastypie.api import Api
from myapp.api import EntryResource

entry_resource = EntryResource()

v1_api = Api(api_name='v1')
v1_api.register(entry_resource)

print entry_resource
print entry_resource.urls
print v1_api

urlpatterns = patterns('',
  (r'^api/', include(entry_resource.urls)),
	(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
)
