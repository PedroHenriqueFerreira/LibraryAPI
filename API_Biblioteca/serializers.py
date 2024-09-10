from rest_framework import serializers
from API_Biblioteca.models import *

# FUNCIONALIDADE NOVA - BLOQUEAR LEITOR DE PEDIR EMPRESTIMO SE TEM ATRASOS
from datetime import datetime, timedelta

# FUNCIONALIDADE NOVA - INCLUIR ISBN E ESTADO DO LIVRO
class Livro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'isbn', 'titulo', 'autor', 'categoria', 'data_pub', 'estado']
        
class Leitor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Leitor
        fields = ['id', 'nome', 'idade', 'cidade'] 


class Emprestimo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'leitor', 'livro', 'data_emprestimo', 'data_devolucao']
    
    # FUNCIONALIDADE NOVA - BLOQUEAR LEITOR DE PEDIR EMPRESTIMO SE TEM ATRASOS
    # FUNCIONALIDADE NOVA - BLOQUEAR LEITOR DE PEDIR MAIS DO QUE 16 EMPRESTIMOS
    def create(self, data):
        leitor = data.get('leitor')
        
        now = datetime.now()
        
        if Emprestimo.objects.filter(leitor=leitor, data_devolucao__isnull=True, data_emprestimo__lt=(now-timedelta(days=30))).exists():
            raise serializers.ValidationError('Leitor com emprestimo em atraso')
        
        if Emprestimo.objects.filter(leitor=leitor, data_devolucao__isnull=True).count() >= 16:
            raise serializers.ValidationError('Leitor com 16 emprestimos ativos')
        
        return super().create(data)