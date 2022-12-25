from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include, re_path
from tienda.views import index
from gestiontienda.views import accesodenegado
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/', include('tienda.urls')),
    path('gestiontienda/', include('gestiontienda.urls')),
    path('',index), 
    path('accesodenegado',accesodenegado)
]

urlpatterns+=[
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root':settings.MEDIA_ROOT,
    })
]
