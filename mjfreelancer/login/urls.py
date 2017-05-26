from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name ='home'),
    url(r'^freelancer/$', views.freelancer_home, name='freelancer_home'),
    url(r'^cadastro/$', views.cadastro , name='cadastro'),
    url(r'^contato/$', views.contato , name='contato'),

    #url(r'^contato/(?P<pk>[0-9]+)/$', views.contato_detail), url(r'^contato/new/$', views.new_contato, name='new_contato'),

]
