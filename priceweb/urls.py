from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^dori', views.dori, name='dori'),
    url(r'^home', views.home, name='home'),
    url(r'^loadingscreens/(?P<index>[0-9]{1})' , views.loadingscreens, name='loadingscreens'),
    url(r'^brewer',views.brewer, name='brewer'),

]