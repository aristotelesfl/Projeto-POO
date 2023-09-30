from models.book_models import *
from models.member_models import *
from models.lib_model import *
from core.lib_core import LibCore

if __name__ == "__main__":
    lib = LibCore()
    membro1 = Membro(1, "ari", "rua", "88888")
    livro1 = LivroFisico(1, "ava", "jjj", 2018, 200)
    lib.cadastrarLivro(livro1)
    lib.cadastrarMembro(membro1)
    lib.listarLivros()
    lib.listarMembros()
