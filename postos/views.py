from django.shortcuts import render,redirect
from folium import Map, Marker
from .models import Posto, Galeria, FotoMapa,Mapa, Imagem, Servico
from .forms import ContatoForm, MapaForm
from django.contrib import messages
import folium
from django.contrib.auth.forms import UserCreationForm




def sobre(request):
    return render(request,'sobre.html')


def rodape(request):
    return render(request, 'rodape.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
def index(request):
    imagens = Imagem.objects.all()[:4]  # Obtém as primeiras 4 imagens
    return render(request, 'index.html', {'imagens': imagens})
# Função para a página inicial
def home(request):
    imagens = Imagem.objects.all()  # Sem limite de imagens
    return render(request, 'postos/home.html', {'imagens': imagens})

# Função para a página do mapa
def mapa(request):
    postos = Posto.objects.all()
    mapa = Map(location=[-23.55052, -46.633308], zoom_start=12)

    # Adicionando marcadores para cada posto
    for posto in postos:
        Marker([posto.latitude, posto.longitude], popup=posto.nome).add_to(mapa)

    return render(request, 'postos/mapa.html', {'mapa': mapa._repr_html_()})

# Função para a página de contatos
# postos/views.py
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.send_email()  # Envia o email (implementar no form)
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})


def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})

# Função para a página da galeria
def galeria(request):
    imagens = Imagem.objects.all()  # Obtém todas as imagens
    return render(request, 'postos/galeria.html', {'imagens': imagens})


# Função para a página de serviços

def servicos(request):
    return render(request, 'postos/servicos.html')

# Função para a página de galeria de fotos
def galeria_fotos(request):
    fotos = FotoMapa.objects.all()
    return render(request, 'postos/galeria_fotos.html', {'fotos': fotos})

# Função para buscar conteúdo
def busca(request):
    query = request.GET.get('q', '')
    resultados = Galeria.objects.filter(nome__icontains=query)  # Filtro básico
    
    # Mensagem caso não encontre resultados
    if not resultados:
        mensagens = "Nenhum resultado encontrado."
    else:
        mensagens = None

    return render(request, 'postos/busca_resultados.html', {'resultados': resultados, 'mensagens': mensagens})

def criar_mapa(request):
    if request.method == 'POST':
        form = MapaForm(request.POST, request.FILES)  # O `request.FILES` é necessário para upload de arquivos
        if form.is_valid():
            form.save()
            messages.success(request, 'Mapa criado com sucesso!')
            return redirect('index')  # Redireciona para a página inicial ou outra página
    else:
        form = MapaForm()

    return render(request, 'criar_mapa.html', {'form': form})

def mapa_upload(request):
    if request.method == 'POST':
        form = MapaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mapa enviado com sucesso!')
            return redirect('mapa_list')  # Redireciona para uma lista de mapas ou outra página
    else:
        form = MapaForm()
    return render(request, 'mapa/upload.html', {'form': form})

def mapa_view(request):
    # Lógica para a visualização do mapa
    return render(request, 'mapa.html')  # Ajuste para o nome correto do template
