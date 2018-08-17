from .models import Configloja, Cliente

class APIConfigLoja:
    """
    API para facilitar o acesso a configloja de configuracao do banco de dados
    """
    def __init__(self):
        conf = Configloja.objects.get(cd_chave='ZIM   1')
        self.cd_regiao, self.sg_loja = conf.no_conf.split(':')[:2]
        self.cd_regiao = int(self.cd_regiao)

class APIConsultaCliente:
    """
    API para utilizar as imagens da aplicação 'CONSULTA'
    """
    def __init__(self, cliente):
        if not isinstance(cliente, Cliente):
            raise Exception('Informe um objeto de Cliente')
        self.conf = APIConfigLoja()
        self.cliente = cliente

    def get_imagens(self):
        """
        Retorna lista de imagens do cliente
        """
        return 'https://{}.claudinosa.com.br/{}/index/{}'.format(
            'theconsulta' if self.conf.sg_loja == 'THE' else self.conf.sg_loja.lower(),
            'api' if self.conf.sg_loja == 'THE' else 'consulta/api',
            str(self.cliente.cd_cliente))
    
    def get_imagem(self, codigo):
        """
        Retorna URL com a imagem do cliente
        """
        return 'https://{}.claudinosa.com.br/{}/get_image/{}'.format(
            'theconsulta' if self.conf.sg_loja == 'THE' else self.conf.sg_loja.lower(),
            'api' if self.conf.sg_loja == 'THE' else 'consulta/api',
            str(codigo))