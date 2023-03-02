class Animal:
    
    def __init__(self, nome, especie, raca, idade) -> None:
        self.__nome = nome 
        self.__especie = especie
        self.__raca = raca
        self.__idade = idade

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade
    
    def setRaca(self, raca):
        self.__raca = raca

    def setEspecie(self, especie):
        self.__especie = especie

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade

    def getRaca(self):
        return self.__raca

    def getEspecie(self):
        return self.__especie


class Consulta:

    def __init__(self, pet: Animal, data, horario, nomeDono):
        self.__pet = pet
        self.__data = data
        self.__horario = horario
        self.__dono = nomeDono

    def setPet(self, pet):
        self.__pet = pet
    
    def setData(self, data):
        self.__data = data
    
    def setHorario(self, horario):
        self.__horario = horario

    def setNomeDono(self, nomeDono):
        self.__dono = nomeDono

    def getPet(self):
        return self.__pet
    
    def getData(self):
        return self.__data
    
    def getHorario(self):
        return self.__horario

    def getNomeDono(self):
        return self.__dono


class clinica:

    def __init__(self):
        self.__name = "Clinica Veterinaria"
        self.__consultas = []

    def agendaConsulta(self, pet, data, horario, dono):
        consulta = Consulta(pet, data, horario, dono)
        if self.__verificarHorario(consulta):
            self.__consultas.append(consulta)
        else:
            print('Horario indisponivel')

    def cancelarConsulta(self, dono):
        for consulta in self.__consultas:
            if consulta.getNomeDono() == dono:
                self.__consultas.remove(consulta)
                return
        print('Consulta Não Encontrada!')    
    



    def listarConsultas(self):
        print('Lista de Consultas agendadas')

        i = 1
        for consulta in self.__consultas:
            print(f'{i}ª Consulta')
            print('Dados do Animal')
            print('=============================')
            print(f'Dono: {consulta.getNomeDono()}')
            print(f'Animal: {consulta.getPet().getNome()}')
            print(f'Especie: {consulta.getPet().getEspecie()}')
            print(f'Raça: {consulta.getPet().getRaca()}')
            print(f'Idade: {consulta.getPet().getIdade()}')
            print('======================================')
            print(f'Data {consulta.getData()}')
            print(f' Horario: {consulta.getHorario()}')
            print('======================================')
            i += 1
            print('\n')

    def __verificarHorario(self, con: Consulta ): 
        for consulta in self.__consultas:
            if consulta.getHorario() == con.getHorario():
                if consulta.getData() == con.getData():
                    return False   
        return True 



clinica = clinica()

pet1 = Animal('Antonio', 'Rato', 'Jubileu', 3)
pet2 = Animal('zeze', 'Cachorro', 'Vira-Lata', 26)
pet3 = Animal('Kennedy', 'Cachorro', 'Buldog', 25)


clinica.agendaConsulta(pet1, '15/02/2023', '16:00', 'Chico da Tripa')
clinica.agendaConsulta(pet2, '25/02/2023', '10:30', 'Manel Sampaio')
clinica.agendaConsulta(pet3, '28/02/2023', '16:00', 'Antonio de Louro')

clinica.listarConsultas()

clinica.cancelarConsulta('Manel Sampaio')

clinica.listarConsultas()
