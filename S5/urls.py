from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('^admin/', admin.site.urls),
    url('', include('website.urls', namespace='website')),
    url('', include('administrator.urls', namespace='administrator')),
    url('', include('authentication.urls', namespace='authentication')),
    url('', include('admission.urls', namespace='admission')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)