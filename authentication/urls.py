from django.conf.urls import url
from . import views

app_name = 'authentication'
urlpatterns = [
    # Account page
    url(r'^account/register/$', views.register, name='login'),
]