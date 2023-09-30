from models.book_models import LivroFisico
from models.member_models import Membro
from models.lib_model import Biblioteca

class LibCore(Biblioteca):
    def __init__(self) -> None:
        super().__init__()

    def cadastrarMembro(self, membro: Membro):
        self.membros.append(membro)
        print("novo membro cadastrado")

    def deletarMembro(self, id):
        for membro in self.membros:
            if membro.id == id:
                self.membros.remove(membro)
                print("membro deletado com sucesso")
            else:
                print("membro não encontrado")
        
    def listarMembros(self):
        for membro in self.membros:
            print("__________________")
            print(f"Id: {membro.id}")
            print(f"Nome: {membro.nome}")
            print(f"Endereço: {membro.endereco}")
            print(f"Telefone: {membro.telefone}")
            
    def cadastrarLivro(self, livro: LivroFisico):
        self.livros.append(livro)
        print("novo livro cadastrado")
    
    def deletarLivro(self, id):
        for livro in self.livros:
            if livro.id == id:
                self.livros.remove(livro)
                print("membro deletado com sucesso")
            else:
                print("membro não encontrado")

    def listarLivros(self):
        for livro in self.livros:
            print("__________________")
            print(f"Id: {livro.id}")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano_publi}")
            print(f"Nº de páginas: {livro.num_pags}\n")
            
