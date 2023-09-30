class Livro:
    def __init__(self, id, autor, titulo, ano_publi):
        self.__id = id
        self.__autor = autor
        self.__titulo = titulo
        self.__ano_publi = ano_publi
        self.__disponivel = True

    def disponivel(self):
        return self.__disponivel

    def emprestimo(self):
        if self.__disponivel:
            self.__disponivel = False
            print("livro emprestado com sucesso")
        else:
            print("livro idisponivel")

    def devolver(self):
        if self.__disponivel:
            self.__disponivel = True
            print("livro devolvido a estante")
        else:
            print("o livro já foi devolvido")
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        self.__autor = value

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def ano_publi(self):
        return self.__ano_publi

    @ano_publi.setter
    def ano_publi(self, value):
        self.__ano_publi = value

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, value):
        self.__disponivel = value

class LivroFisico(Livro):
    def __init__(self, id, autor, titulo, ano_publi, num_pags):
        super().__init__(id, autor, titulo, ano_publi)
        self.__num_pags = num_pags

    @property
    def num_pags(self):
        return self.__num_pags

    @num_pags.setter
    def num_pags(self, value):
        self.__num_pags = value

class LivroDigital(Livro):
    def __init__(self, id, autor, titulo, ano_publi, formato):
        super().__init__(id, autor, titulo, ano_publi)
        self.__formato = formato

    @property
    def formato(self):
        return self.__formato

    @formato.setter
    def formato(self, value):
        self.__formato = value
