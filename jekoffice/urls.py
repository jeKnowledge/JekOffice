from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('processos/', include('processos.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('salas/', include('gestao_salas.urls')),
    path('interno/',include('interno.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
