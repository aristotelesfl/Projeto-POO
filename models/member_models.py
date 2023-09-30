from .book_models import LivroFisico

class Membro:
    def __init__(self, id, nome, endereco, telefone) -> None:
        self.__id = id
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__emprestados = []    

    def emprestarLivro(self, livro: LivroFisico):
        if livro.disponivel():
            self.__emprestados.append(livro)
            livro.emprestimo()

    def devolverLivro(self, livro: LivroFisico):
        if livro in self.__emprestados:
            self.__emprestados.remove(livro)
            livro.devolver
        else:
            print("Livro não encontrado")

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

