from rest_framework import (
    serializers, 
    viewsets,
)
from crediario.clientes.models import Cliente


# Serializers define the API representation.
class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

