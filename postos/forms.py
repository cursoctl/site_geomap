
from django import forms
from .models import Posto, Mapa


class MapaForm(forms.ModelForm):
    class Meta:
        model = Mapa
        fields = ['nome', 'descricao', 'likes'] 

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # Lógica para enviar e-mail, se necessário
        pass

