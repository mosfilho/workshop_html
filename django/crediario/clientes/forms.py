from django import forms
from crediario.clientes.models import Cliente, Tablinha
from datetime import datetime

CHOICES_GENERO = (
    ('M','Masculino'),
    ('F','Feminino'),
)

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