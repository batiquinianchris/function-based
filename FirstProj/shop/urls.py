from django.conf.urls import url
from . import views


app_name = 'shop'

urlpatterns = (

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list$', views.technician_list, name='tech_list'),
    url(r'^new$$', views.technician_create, name='tech_new'),
    url(r'^edit/(?P<pk>\d+)$', views.technician_update, name='tech_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.technician_delete, name='tech_delete'),

)
