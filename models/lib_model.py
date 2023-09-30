class Biblioteca:
    def __init__(self) -> None:
        self.__livros = []
        self.__membros = []

    @property
    def livros(self):
        return self.__livros

    @livros.setter
    def livros(self, value):
        self.__livros = value

    @property
    def membros(self):
        return self.__membros

    @membros.setter
    def membros(self, value):
        self.__membros = value

