from django.conf.urls import url
from . import views

app_name = 'admission'
urlpatterns = [
    # Account page
    # url(r'^apply/$', views.ApplyView.as_view(), name='apply'),
    url(r'^apply/(?P<id>\d+)$', views.apply, name='apply'),
]