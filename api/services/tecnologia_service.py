from django.http import Http404
from ..models import Tecnologia

#---------------------------------------------------------------------------------LISTAR TECNOLOGIAS
def listar_tecnologias():
    #relizando uma busca de todas as tecnologias
    tecnologias = Tecnologia.objects.all()
    #rertonando o resultados da busca
    return tecnologias


def cadastrar_tecnologia(tecnologia):
    #buscando e retornando o objeto a ser criado com seus devidos campos
    return Tecnologia.objects.create(nome=tecnologia.nome)


def listar_tecnologia_id(id):
    #tratamento para verificar se o id passado exite
    try:
        #retornando uma tecnologia especifica pelo id
        return Tecnologia.objects.get(id=id)
    #caso o id não exita, será retornado o objetos com erro 404
    except Tecnologia.DoesNotExist:
        raise Http404


def editar_tecnologia(tecnologia_antiga, tecnologia_nova):
    #substituindo as infomações
    tecnologia_antiga.nome = tecnologia_nova.nome
    #salvando a nova tecnologia no banco
    tecnologia_antiga.save(force_update=True)


def remover_tecnologia(tecnologia):
    #removendo a tecnologia do banco
    tecnologia.delete()