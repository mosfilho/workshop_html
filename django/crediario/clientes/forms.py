from django import forms
from crediario.clientes.models import Cliente, Tablinha
from datetime import datetime

CHOICES_GENERO = (
    ('M','Masculino'),
    ('F','Feminino'),
)

CHOICES_TIPO_BUSCA_CLIENTE = (
    ('0', 'Código'),
    ('1', 'Nome'),
)

class ClienteBuscaForm(forms.Form):
    sg_loja = forms.CharField(max_length=3, disabled=True)
    cd_regiao = forms.IntegerField(disabled=True)
    tipo = forms.ChoiceField(choices=CHOICES_TIPO_BUSCA_CLIENTE)
    valor = forms.CharField(max_length=100, initial=203114)

    def clean(self):
        cleaned_data = super().clean()

        if  cleaned_data['tipo'] == "0" and not cleaned_data['valor'].isdigit():
            self.add_error("valor","Informe um código válido")

        return cleaned_data
    

class ClienteForm(forms.ModelForm):
    cd_sexo = forms.ChoiceField(choices=CHOICES_GENERO, label='Gênero')
    
    class Meta:
        model = Cliente
        fields = '__all__' # pega todos os fields do modelo
        #fields = ['cd_sexo','dt_nascimento',] # define alguns campos para o formulário

    def clean_dt_nascimento(self):
        """
        Valida campo de data de nascimento.
        """
        data = self.cleaned_data['dt_nascimento']
        
        if data < datetime(1958,1,1).date():
            self.add_error('dt_nascimento', 'Nasceu antes do ano do Paraíba!')
        
        return data