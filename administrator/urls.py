from django.conf.urls import url
from . import views

app_name = 'administrator'
urlpatterns = [
    # Home page
    url(r'^dashboard/(?P<id>\d+)/$', views.index, name='index'),
    # show all schools
    url(r'school/all_school', views.all_school, name="all_school"),
    # Registration page
    url(r'school/register-school', views.register, name="register"),
    # view a specific school
    url(r'school/(?P<id>\d+)/$', views.view_school, name="view_school"),
    # url(r'add_new_school_admin/(?P<id>\d+)/$', views., name="view_school"),
]