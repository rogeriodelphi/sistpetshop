from ..models import Pet

def cadastrar_pet(pet):
    pet_bd = Pet.objects.create(nome=pet.nome, nascimento=pet.nascimento, categoria=pet.categoria,
                                cor=pet.cor, dono=pet.dono)
    pet_bd.save()
