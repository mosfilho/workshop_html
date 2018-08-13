from django.shortcuts import render
from crediario.clientes.forms import ClienteForm

# Create your views here.
def vw_cadastro_cliente(request):
    form = ClienteForm()
    return render(request, 
        'clientes/cadastro.html',
        {
            'form': form
        }
    )