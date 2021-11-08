from ..models import ConsultaPet

def cadastar_consulta(consulta):
    consulta_bd = ConsultaPet.objects.create(pet=consulta.pet, motivo_consulta=consulta.motivo_consulta,
                                             peso_atual=consulta.peso_atual,
                                             medicamento_atual=consulta.medicamento_atual,
                                             medicamentos_prescritos=consulta.medicamentos_prescritos,
                                             exames_prescritos=consulta.exames_prescritos)
    consulta_bd.save()


# filtro para retorna apenas o pet que posssue o determinado ID
def listar_consultas(id):
    consultas = ConsultaPet.objects.filter(pet=id).all()
    return consultas


# filtro para retorna as consultas em que o ID do dono do pet é igual
# aquele ID que está sendo passado
def listar_consultas_pets(id):
    consultas = ConsultaPet.objects.filter(pet__dono=id).all().order_by('-data')
    return consultas