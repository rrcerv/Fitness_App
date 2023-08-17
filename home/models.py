from django.db import models
from usuarios.models import Usuario


class Configuracoes(models.Model):

    class Niveis(models.TextChoices):
        INICIANTE = 'Iniciante'
        INTERMEDIARIO = 'Intermediário'
        AVANCADO = 'Avançado'

    class Categorias(models.TextChoices):
        HIPERTROFIA = 'Hipertrofia'
        RESISTENCIA = 'Resistência'
        FORCA = 'Força'

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    niveis = models.TextField(choices=Niveis.choices)
    categorias = models.TextField(choices=Categorias.choices)



class Exercicios(models.Model):
    parte_corpo = models.TextField()
    equipamento = models.TextField()
    gif = models.TextField()
    nome = models.TextField()
    alvo = models.TextField()


class Usuario_Treinos(models.Model):
    
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    class Treinos(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'

    class Grupo_muscular(models.TextChoices):
        PEITO = 'Peito'
        COSTAS = 'Costas'
        BICEPS = 'Bíceps'
        TRICEPS = 'Triceps'
        PERNA = 'Perna'
        ABDOMEN = 'Abdomen'
        NENHUM = 'Nenhum'

    treino = models.TextField(choices=Treinos.choices)
    
    grupo_muscular1 = models.TextField(choices=Grupo_muscular.choices)
    grupo_muscular2 = models.TextField(choices=Grupo_muscular.choices)  

    exercicios = models.ManyToManyField(Exercicios)
    data = models.DateField()

class Curiosidades(models.Model):
    curiosidade = models.TextField()