from rest_framework import serializers
from ..models import Tecnologia

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        #model a ser utilizada
        model = Tecnologia
        #definindo os campos a ser passados
        fields = ('id', 'nome', )