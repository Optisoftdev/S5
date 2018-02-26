from django.conf.urls import url
from . import views

app_name = 'website'
urlpatterns = [
    # Account page
    url(r'^$', views.index, name='index'),
]