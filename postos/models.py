from django.db import models

class Posto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='postos/')
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Posto'
        verbose_name_plural = 'Postos'

class Imagem(models.Model):
    photo = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return str(self.photo.name)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


class Mapa(models.Model):
    nome = models.CharField(max_length=100)  # Nome do mapa
    descricao = models.TextField()  # Descrição do mapa
    imagem = models.ImageField(upload_to='mapas/')  # Imagem associada ao mapa
    # Adicionando o campo 'titulo', se necessário
    titulo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class FotoMapa(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='fotos_mapas/')  # Define o local onde as imagens serão armazenadas.
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    

class Galeria(models.Model):
    # Defina os campos do modelo Galeria
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='galeria/')

class Mapa(models.Model):
    nome = models.CharField(max_length=100)  # Nome do mapa
    descricao = models.TextField()  # Descrição do mapa
    imagem = models.ImageField(upload_to='mapas/')  # Imagem associada ao mapa
    titulo = models.CharField(max_length=100, blank=True, null=True)
    likes = models.IntegerField(default=0)  # Campo likes adicionado

    def __str__(self):
        return self.nome