
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from postos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Adicionando URL para a página inicial
    path('postos/', include('postos.urls')),  # Incluindo URLs do app mapa
]

# Configuração para servir arquivos de mídia no modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)