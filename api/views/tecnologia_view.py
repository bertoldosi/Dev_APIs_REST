from rest_framework.views import APIView
from ..services import tecnologia_service
from ..serializers import tecnologia_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import tecnologia

class TecnologiaList(APIView):


    def get(self, request, format=None):
        # Buscar todas tecnologias filtradas no service
        tecnologias = tecnologia_service.listar_tecnologias()
        #validar os dados repassados pelo service. 'many' diz que a varias tecnologias sendo enviadas
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        #retonar todas as tecnologias. 'status' dever ser repassado quando toda requisição http está correta.
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        #enviando o nome para o serializer verificar se o dado do request está de acordo com as regras(se é CharFild, IntegerFild)
        serializer = tecnologia_serializer.TecnologiaSerializer(data=request.data)
        #caso esse serializer seja valido entra no if
        if serializer.is_valid():
            #pegando o nome enviado pela requisição
            nome = serializer.validated_data['nome']
            #criando um objeto do tipo Tecnologia
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            #inserido essa tecnologia no banco de dados
            tecnologia_bd = tecnologia_service.cadastrar_tecnologia(tecnologia_nova)
            #retonar o 'serializer.data' no caso os dados da tecnologia cadastrada, e status da operação
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #caso dê algo errado no request, retornamos o 'serializer.errors' para indicar o erro, e status da operação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TecnologiaDetalhes(APIView):


    def get(self, request, id, format=None):
        #pegando a tecnologia do service
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        #verificando atraves do serializer se está de acordo com as regras
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia)
        #retornado o serializer e o status da operação
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        #pegando a tecnologia filtrada no service
        tecnologia_antiga = tecnologia_service.listar_tecnologia_id(id)
        #realizando a validação dessa tecnologia atraves do serializer
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia_antiga, data=request.data)
        #serializer seno valido
        if serializer.is_valid():
            # atribui a informação na variavel nome
            nome = serializer.validated_data['nome']
            #criamos uma nova tecnologia que ser alterada no bando de dados
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            #chama o metodo de edição e passar as duas informações
            tecnologia_service.editar_tecnologia(tecnologia_antiga, tecnologia_nova)
            #retornando a nossa nova ternologia(serializer) e passando o status da operação
            return Response(serializer.data, status=status.HTTP_200_OK)
        #caso algo de errado com o request, passado o erro, e o staus da operação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        #pegando a tecnologia a ser removida atraves do service
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        #passando a tecnologia para o service para ser removida
        tecnologia_service.remover_tecnologia(tecnologia)
        #retornando apos a remoção, mostrando somente o status da operação
        return Response(status=status.HTTP_204_NO_CONTENT)