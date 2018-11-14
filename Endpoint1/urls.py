from django.conf.urls import url,include
from . import views
app_name = 'endpoint1'

urlpatterns = [
    url(r'^$', views.Json_response.as_view(), name='json_response'),
    url(r'^stats/$', views.req_count, name='stats')
]
