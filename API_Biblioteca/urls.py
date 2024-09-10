from rest_framework.routers import SimpleRouter
from API_Biblioteca.views import *

# gerador automático de urls do rest
router = SimpleRouter()
router.register('livros', Livro_API)
router.register('leitores', Leitor_API)
router.register('emprestimos', Emprestimo_API)

urlpatterns = [
    # outras urls do seu projeto
    
]