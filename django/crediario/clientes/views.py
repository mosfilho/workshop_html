from django.shortcuts import render
from crediario.clientes.models import Cliente, Configloja
from crediario.clientes.forms import ClienteBuscaForm

# Create your views here.
def vw_clientes(request):
    data = {}
    conf = Configloja.objects.get(cd_chave='ZIM   1')
    data['cd_regiao'], data['sg_loja'] = conf.no_conf.split(':')[:2]
    data['cd_regiao'] = int(data['cd_regiao'])
    form = ClienteBuscaForm(initial=data)

    if request.method == 'POST':
        print("POST DANADO")

    return render(request, 
        'clientes/change_list.html',
        {
            'form': form
        }
    )