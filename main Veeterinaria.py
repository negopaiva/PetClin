class Animal:

    def __init__(self, nome: str, especie: str, raca: str, idade: int) -> None:
        self.__nome = nome
        self.__especie = especie
        self.__raca = raca
        self.__idade = idade

    def setNome(self, nome: str) -> None:
        self.__nome = nome

    def setEspecie(self, especie: str) -> None:
        self.__especie = especie

    def setRaca(self, raca: str) -> None:
        self.__raca = raca

    def setIdade(self, idade: int) -> None:
        self.__idade = idade

    def getNome(self) -> str:
        return self.__nome

    def getEspecie(self) -> str:
        return self.__especie

    def getRaca(self) -> str:
        return self.__raca

    def getIdade(self) -> int:
        return self.__idade


class Consulta:

    def __init__(self, pet: Animal, data: str, horario: str, nomeDono: str) -> None:
        self.__pet = pet
        self.__data = data
        self.__horario = horario
        self.__dono = nomeDono

    def getPet(self) -> Animal:
        return self.__pet

    def getData(self) -> str:
        return self.__data

    def getHorario(self) -> str:
        return self.__horario

    def getNomeDono(self) -> str:
        return self.__dono


class Clinica:

    def __init__(self) -> None:
        self.__name = 'Clinica Pet Morto'
        self.__consultas = []

    def agendarConsulta(self, pet: Animal, data: str, horario: str, dono: str) -> None:
        consulta = Consulta(pet, data, horario, dono)
        if self.__verificarHorario(consulta):
            self.__consultas.append(consulta)
        else:
            print(f'Desculpe {dono} já existe uma consulta marcada nesse horario, tente novamente em outro horário.')

    def listarConsultasAgendadas(self) -> None:
        print(f'***Bem vindo a {self.__name}***')
        print('***LISTA DE CONSULTAS AGENDADAS***')
        c = 1
        for consulta in self.__consultas:
            print(f'{c}ª Consulta')
            print('DADOS DO ANIMAL')
            print(f'Nome do dono: {consulta.getNomeDono()}')
            print(f'Nome do animal: {consulta.getPet().getNome()}')
            print(f'Especie: {consulta.getPet().getEspecie()}')
            print(f'Raça: {consulta.getPet().getRaca()}')
            print(f'Idade: {consulta.getPet().getIdade()}')
            print('-------------------------------------')
            print(f'Data: {consulta.getData()}')
            print(f'Horario: {consulta.getHorario()}')
            print('-------------------------------------')
            print(' ')
            c += 1

    def __verificarHorario(self, con: Consulta) -> bool:
        for consulta in self.__consultas:
            if consulta.getHorario() == con.getHorario():
                if consulta.getData() == con.getData():
                    return False

        return True


clinica = Clinica()

pet1 = Animal('Bola de neve', 'Gato', 'Siamês', 3)
pet2 = Animal('Rex', 'Cachorro', 'Pitbull', 2)
pet3 = Animal('Marrie', 'Cachorro', 'Pincher', 3)

clinica.agendarConsulta(pet1, '15/03/2023', '15:35', 'Maria Tavares')
clinica.agendarConsulta(pet2, '16/08/2023', '9:45', 'David Jose')
clinica.agendarConsulta(pet3, '16/08/2023', '9:45', 'Josefa Maria')

clinica.listarConsultasAgendadas()
