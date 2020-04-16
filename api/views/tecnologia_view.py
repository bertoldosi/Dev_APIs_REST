from rest_framework.views import APIView
from ..services import tecnologia_service
from ..serializers import tecnologia_serializer
from rest_framework.response import Response
from rest_framework import status


class TecnologiaList(APIView):

    def get(self, request, format=None):
        # Buscar todas tecnologias filtradas no service
        tecnologias = tecnologia_service.listar_tecnologias()
        #validar os dados repassados pelo service. 'many' diz que a varias tecnologias sendo enviadas
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        #retonar todas as tecnologias. 'status' dever ser repassado quando toda requisição http está correta.
        return Response(serializer.data, status=status.HTTP_200_OK)