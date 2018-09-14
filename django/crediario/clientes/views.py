from django.shortcuts import render
from crediario.clientes.models import Cliente, Configloja, APIConfigLoja
from crediario.clientes.forms import ClienteBuscaForm
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings


def vw_clientes(request):
    data = {}
    context = {}
    conf = Configloja.objects.get(cd_chave='ZIM   1')
    data['cd_regiao'], data['sg_loja'] = conf.no_conf.split(':')[:2]
    data['cd_regiao'] = int(data['cd_regiao'])
    form = ClienteBuscaForm(initial=data)
        
    if request.method == 'POST':
        form = ClienteBuscaForm(initial=data, data=request.POST)

        if form.is_valid():

            clientes = Cliente.objects.none()

            if form.cleaned_data['tipo'] == '0': # buscar pelo código
                cd_chave = '{0}{1}'.format(
                    str(form.cleaned_data['cd_regiao']).rjust(2),
                    form.cleaned_data['valor'].strip().rjust(8))
                clientes = Cliente.objects.filter(cd_chave = cd_chave)
            else: # buscar pelo nome
                clientes = Cliente.objects.filter(cd_nomcod__istartswith=form.cleaned_data['valor'])

            context['clientes'] = clientes

            if clientes.count() == 0:
                messages.add_message(request, messages.INFO, 'Cliente inexistente')


    context['form'] = form

    return render(request, 
        'clientes/change_list.html',
        context
    )


def vw_api_imagem_cliente(request, codigo):
    conf = APIConfigLoja()
    chave = '{0}{1}'.format(
        str(conf.cd_regiao).rjust(2),
        str(codigo).rjust(8))

    cliente = Cliente.objects.filter(cd_chave=chave)

    if cliente.count == 0:
        return JsonResponse([], safe=False)

    imagem = cliente[0].get_foto()

    return JsonResponse(imagem if imagem else [], safe=False)
    