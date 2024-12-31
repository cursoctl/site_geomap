from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('mapa/', views.mapa, name='mapa'),
    path('contato/', views.contato, name='contato'),
    path('galeria/', views.galeria, name='galeria'),
    path('galeria/fotos/', views.galeria_fotos, name='galeria_fotos'),
    path('busca/', views.busca, name='busca'),
    path('servicos/',views.servicos, name='servicos'),
    path('rodape/', views.rodape, name='rodape'),
    path('sobre/', views.sobre, name='sobre'),
    # Usando a view de login padrão do Django
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    # Usando a view de logout padrão do Django
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# URLs de funcionalidades relacionadas a mapas
mapa_patterns = [
    path('mapa/', views.mapa_view, name='mapa'),  # Visualização de mapa
    path('criar/mapa/', views.criar_mapa, name='criar_mapa'),  # Criar novo mapa
    path('mapa/upload/', views.mapa_upload, name='mapa_upload'),  # Upload de mapa
]

# Combinação de todas as URLs
urlpatterns += mapa_patterns  # Corrigido para adicionar mapa_patterns a urlpatterns

# Adiciona URLs para arquivos de mídia apenas se estiver no modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
