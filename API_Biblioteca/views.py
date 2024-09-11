from rest_framework import viewsets, permissions
from API_Biblioteca.models import Livro, Leitor, Emprestimo
from API_Biblioteca.serializers import LivroSerializer, LeitorSerializer, EmprestimoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class LivroAPI(viewsets.ModelViewSet):
    '''API para gerenciamento de livros'''
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    # FUNCIONALIDADE NOVA - FILTRO DE LIVROS POR TITULO E ISBN
    def get_queryset(self):
        queryset = self.queryset
        
        query_set = queryset.filter(titulo__icontains=self.request.query_params.get('titulo', ''))
        query_set = query_set.filter(isbn__icontains=self.request.query_params.get('isbn', ''))
        
        return query_set


class LeitorAPI(viewsets.ModelViewSet):
    '''API para gerenciamento de leitores'''
    queryset = Leitor.objects.all()
    serializer_class = LeitorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    # traz todos os emprestimos de um usuario
    @action(detail=True, methods=['get'])
    def emprestimos(self, request, pk=None):
        leitor = self.get_object()
        emprestimos = Emprestimo.objects.filter(leitor=leitor)
        serializer = EmprestimoSerializer(emprestimos, many=True)
        return Response(serializer.data)


class EmprestimoAPI(viewsets.ModelViewSet):
    '''API para gerenciamento de emprestimos'''
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

