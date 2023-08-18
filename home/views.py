from django.shortcuts import render, redirect
import os
from pathlib import Path
from .models import Usuario, Exercicios, Usuario_Treinos, Configuracoes, Curiosidades
import requests
import random
from datetime import date
from django.core.paginator import Paginator

def passando_curiosidades():
    curiosidades = [
    "Arnold Schwarzenegger venceu o concurso de fisiculturismo Mr. Olympia um recorde de 7 vezes.",
    "Levantamento de peso tornou-se um esporte olímpico oficial em 1896.",
    "O maior músculo do corpo humano é o glúteo máximo.",
    "O CrossFit foi fundado em 2000 por Greg Glassman e Lauren Jenai.",
    "Treinamento intervalado de alta intensidade (HIIT) queima mais calorias em menos tempo do que cardio de intensidade constante.",
    "O conceito do Pilates foi desenvolvido por Joseph Pilates no início do século 20.",
    "Em 2020, a indústria global de fitness foi avaliada em US$ 96,7 bilhões.",
    "O Yoga teve origem na antiga Índia há mais de 5.000 anos.",
    "Uma pessoa em repouso queima aproximadamente 150 calorias por hora enquanto dorme.",
    "O levantamento terra trabalha mais músculos do que qualquer outro exercício.",
    "O icônico slogan da Nike 'Just Do It' foi inspirado nas últimas palavras de um homem antes da execução.",
    "O recorde mundial de flexões em uma hora é de 2.806.",
    "Os primeiros Jogos Olímpicos modernos foram realizados em Atenas, Grécia, em 1896.",
    "O boxe é um dos esportes mais antigos conhecidos, com mais de 5.000 anos de história.",
    "O mais antigo halter conhecido data da Grécia antiga, por volta de 200 a.C.",
    "Pular corda pode queimar até 1.000 calorias por hora.",
    "A maratona mais rápida já concluída foi em 1 hora, 59 minutos e 40 segundos por Eliud Kipchoge.",
    "O levantamento de peso pode melhorar a densidade óssea e reduzir o risco de osteoporose.",
    "Uma pessoa média caminha o equivalente a três vezes ao redor do mundo em toda a sua vida.",
    "O agachamento é considerado o rei de todos os exercícios.",
    "Serena Williams, uma das maiores jogadoras de tênis, também é uma frequentadora assídua de academia.",
    "Nadar é um exercício de baixo impacto que trabalha todo o corpo.",
    "O exercício de supino foi popularizado pelo fisiculturista e empresário Joe Weider.",
    "Muhammad Ali, o lendário pugilista, era conhecido por sua velocidade e agilidade no ringue.",
    "A primeira academia comercial nos Estados Unidos foi aberta em Santa Monica, Califórnia, em 1933.",
    "As kettlebells eram originalmente usadas como contrapesos nos mercados russos.",
    "Uma pessoa média possui cerca de 600 músculos.",
    "O fisiculturista Ronnie Coleman detém o recorde de mais vitórias no Mr. Olympia, com 8 títulos.",
    "O fisiculturista Ronnie Coleman detém o recorde de mais vitórias no Mr. Olympia, com 8 títulos.",
    "Os halteres foram usados pela primeira vez na Grécia antiga como pesos de levantamento para atletas.",
    "A ginástica remonta à Grécia antiga e foi incluída nos primeiros Jogos Olímpicos modernos.",
    "Michael Phelps, o maior medalhista olímpico de todos os tempos, consome cerca de 12.000 calorias por dia durante os treinos.",
    "Agachamentos não são bons apenas para a força das pernas, mas também para o desenvolvimento do core.",
    "O treinamento com pesos pode ajudar a melhorar a função cognitiva e a memória.",
    "O jogador de basquete LeBron James é conhecido por seus intensos treinos de academia.",
    "Uma pessoa média realiza entre 17.000 e 30.000 respirações por dia.",
    "Os levantamentos terra receberam esse nome devido à ação de levantar um peso inerte do chão.",
    "O levantamento de peso faz parte dos Jogos Paralímpicos desde sua criação em 1960.",
    "Os dispositivos de rastreamento de fitness, como o Fitbit, ganharam popularidade no final dos anos 2000.",
    "O exercício regular pode ajudar a reduzir os sintomas de depressão e ansiedade.",
    "A frequência cardíaca de repouso média de uma pessoa adulta é cerca de 60 a 100 batimentos por minuto.",
    "O fisiculturista Jay Cutler venceu o Mr. Olympia em 2006, 2007, 2009 e 2010.",
    "O treinamento de resistência pode ajudar a aumentar o metabolismo e queimar mais calorias em repouso.",
    "A flexão é um exercício eficaz para fortalecer os músculos do peito, ombros e braços.",
    "A bicicleta ergométrica foi inventada no final do século XIX como uma forma de treinamento indoor.",
    "O treinamento de força pode ajudar a prevenir lesões e melhorar a saúde das articulações.",
    "O atleta Usain Bolt detém o recorde mundial dos 100 metros rasos, com um tempo de 9,58 segundos.",
    "A Zumba, uma forma de exercício aeróbico baseado em dança, foi criada na década de 1990 pelo coreógrafo Alberto Perez.",
    "A flexibilidade é importante para melhorar o desempenho atlético e reduzir o risco de lesões.",
    "O exercício regular pode melhorar a qualidade do sono e ajudar a combater a insônia.",
    "A caminhada rápida é uma forma eficaz de exercício aeróbico que pode ajudar a queimar calorias e melhorar a saúde cardiovascular.",
    "O treinamento com pesos pode ajudar a melhorar a postura e prevenir dores nas costas.",
    "O fisiculturista Lee Haney venceu o Mr. Olympia em 1984, 1985, 1986, 1987, 1988, 1989 e 1990.",
    "A natação é um exercício de baixo impacto que fortalece os músculos e melhora a resistência cardiovascular.",
    "A atividade física regular pode ajudar a reduzir o risco de doenças cardíacas, diabetes e alguns tipos de câncer.",
    "O alongamento dinâmico, que envolve movimentos ativos, é mais eficaz antes do exercício do que o alongamento estático.",
    "A escalada em rocha é um esporte desafiador que requer força, equilíbrio e habilidade mental.",
    "O treinamento intervalado de alta intensidade (HIIT) pode melhorar a capacidade cardiovascular e queimar mais gordura.",
    "O fisiculturista Dorian Yates venceu o Mr. Olympia por seis anos consecutivos, de 1992 a 1997.",
    "O exercício regular pode ajudar a reduzir a pressão arterial e melhorar a saúde do coração.",
    "O levantamento de peso ajuda a fortalecer os ossos e reduzir o risco de osteoporose.",
    "O treinamento de resistência pode ajudar a aumentar a força muscular e a resistência.",
    "O fisiculturista Phil Heath venceu o Mr. Olympia em 2011, 2012, 2013, 2014, 2015 e 2016.",
    "A meditação pode ser uma prática útil para melhorar o foco mental e reduzir o estresse.",
    "A música pode ajudar a aumentar a motivação e o desempenho durante o exercício físico.",
    "O treinamento com pesos não só ajuda a construir músculos, mas também acelera o metabolismo.",
    "O sono adequado é essencial para a recuperação muscular e o desempenho físico.",
    "O treinamento de circuito, que combina exercícios cardiovasculares e de força, pode ser eficaz para queimar calorias e melhorar a aptidão geral.",
    "A dieta desempenha um papel fundamental no desempenho atlético e na composição corporal.",
    "O treinamento de alta intensidade pode continuar a queimar calorias mesmo após o término do exercício.",
    "A musculação não torna as mulheres volumosas, mas ajuda a tonificar os músculos e melhorar a definição.",
    "O estresse crônico pode afetar negativamente a saúde e o desempenho físico.",
    "A prática regular de ioga pode ajudar a melhorar a flexibilidade, o equilíbrio e a reduzir o estresse.",
    "O treinamento de intervalo pode ajudar a melhorar a resistência cardiovascular e a queima de gordura.",
    "A prática de exercícios físicos libera endorfinas, substâncias químicas que proporcionam uma sensação de bem-estar."
  ]
    for curiosidade in curiosidades:
        curiosidade_db = Curiosidades(curiosidade=curiosidade)
        curiosidade_db.save()

def gerar_treino(usuario, parte_corpo, alvo, letra_treino, grupo_muscular1, grupo_muscular2):                
    if not (Usuario_Treinos.objects.filter(usuario=usuario, treino=letra_treino)):     #Se o usuario não tem treinos
        print('Certo')
        exercicios = Exercicios.objects.filter(parte_corpo=parte_corpo)
        
        exercicios1 = Exercicios.objects.filter(parte_corpo=parte_corpo)
        exercicios2= Exercicios.objects.filter(alvo=alvo)

        usuario_exercicios1 = []
        usuario_exercicios2 = []

        for a in range(5):
            usuario_exercicios1.append(random.choice(exercicios1))

        for a in range(3):
            usuario_exercicios2.append(random.choice(exercicios2))

        data_atual = date.today()
        data_formatada = data_atual.isoformat()

        novo_treino = Usuario_Treinos(usuario=usuario, treino=letra_treino , grupo_muscular1=grupo_muscular1, grupo_muscular2=grupo_muscular2, data=data_formatada)
        novo_treino.save()

        novo_treino.exercicios.add(*usuario_exercicios1)
        novo_treino.exercicios.add(*usuario_exercicios2)
    
    
    else:  #Se o usuário tiver treinos
        treinos_usuario = Usuario_Treinos.objects.filter(usuario=usuario, treino=letra_treino)
        for treino in treinos_usuario:
            treino.delete()
        
        exercicios = Exercicios.objects.filter(parte_corpo=parte_corpo)
        
        exercicios1 = Exercicios.objects.filter(parte_corpo=parte_corpo)
        exercicios2= Exercicios.objects.filter(alvo=alvo)

        usuario_exercicios1 = []
        usuario_exercicios2 = []

        for a in range(5):
            usuario_exercicios1.append(random.choice(exercicios1))

        for a in range(3):
            usuario_exercicios2.append(random.choice(exercicios2))

        data_atual = date.today()
        data_formatada = data_atual.isoformat()

        novo_treino = Usuario_Treinos(usuario=usuario, treino=letra_treino , grupo_muscular1=grupo_muscular1, grupo_muscular2=grupo_muscular2, data=data_formatada)
        novo_treino.save()

        novo_treino.exercicios.add(*usuario_exercicios1)
        novo_treino.exercicios.add(*usuario_exercicios2)

def atualizar_links():
    import requests

    url = "https://exercisedb.p.rapidapi.com/exercises"

    headers = {
    	"X-RapidAPI-Key": "6b34606cc8msh2818f266c6eeb21p1fd579jsncd75030f06ba",
    	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    

    for exercicio in data:
        ex_db = Exercicios.objects.get(nome=exercicio['name'], alvo=exercicio['target'], equipamento=exercicio['equipment'], parte_corpo=exercicio['bodyPart'])
        ex_db.gif = exercicio['gifUrl']
        ex_db.save()

def limpar_duplicatas():
    ultimo_nome_visto = ''
    rows = Exercicios.objects.all().order_by('nome')

    for exercicio in rows:
        if exercicio.nome == ultimo_nome_visto:
            exercicio.delete()
        else:
            ultimo_nome_visto = exercicio.nome

def home(request):
    #CHECA SE O USUÁRIO ESTÁ LOGADO
    if request.session.get('usuario'):
        #DEFINE O USUÁRIO
        status = request.GET.get('status')
        usuario_id = request.session.get('usuario')
        usuario = Usuario.objects.get(id=usuario_id)
        exercicios = []
        nome = (str(usuario.nome)).title()
        atualizar_links()
        
        #CHECA SE O USUÁRIO TEM TREINOS, CASO NÃO GERA OS TREINOS DELE.
        if not Usuario_Treinos.objects.filter(usuario=usuario):
            gerar_treino(usuario=usuario, parte_corpo='chest', alvo='biceps', letra_treino='A', grupo_muscular1='Peito', grupo_muscular2='Bíceps')
            gerar_treino(usuario=usuario, parte_corpo='back', alvo='triceps', letra_treino='B', grupo_muscular1='Costas', grupo_muscular2='Triceps')
            gerar_treino(usuario=usuario, parte_corpo='lower legs', alvo='abs', letra_treino='C', grupo_muscular1='Perna', grupo_muscular2='Abdomen')

        #SEPARA OS TREINOS
        treinoa = Usuario_Treinos.objects.get(usuario = usuario, treino='A')
        treinob = Usuario_Treinos.objects.get(usuario=usuario, treino='B')
        treinoc = Usuario_Treinos.objects.get(usuario=usuario, treino='C')
        treinoa = treinoa.exercicios.all()
        treinob = treinob.exercicios.all()
        treinoc = treinoc.exercicios.all()

        #USA O PAGINATOR PARA SEPARAR DE 4 EM 4 EXERCÍCIOS
        paginator_treinoa = Paginator(treinoa, 4)
        treinoa_pag1 = paginator_treinoa.get_page(1)
        treinoa_pag2 = paginator_treinoa.get_page(2)

        paginator_treinob = Paginator(treinob, 4)
        treinob_pag1 = paginator_treinob.get_page(1)
        treinob_pag2 = paginator_treinob.get_page(2)

        paginator_treinoc = Paginator(treinoc, 4)
        treinoc_pag1 = paginator_treinoc.get_page(1)
        treinoc_pag2 = paginator_treinoc.get_page(2)

        #Selecionando 8 curiosidades aleatórias
        curiosidades = []
        todas_curiosidades = Curiosidades.objects.all()
        for i in range(8):
            curiosidades.append(random.choice(todas_curiosidades))
            
     
        
        try:
             configuracoes = Configuracoes.objects.get(usuario=usuario)
             print('Há configurações')
             return render(request, 'home.html', {'status': status, 'exercicios': exercicios, 'treinoa_pag1': treinoa_pag1, 'treinoa_pag2': treinoa_pag2,
                                                  'treinob_pag1': treinob_pag1, 'treinob_pag2': treinob_pag2, 'treinoc_pag1': treinoc_pag1, 'treinoc_pag2': treinoc_pag2, 
                                                  'nome': nome, 'curiosidades': curiosidades})
        

        except:
             print('Não há configurações')
             return redirect('configuracoes')
    
    else:
        return redirect('/auth/login/?status=2')

def configuracoes(request):
      
    if request.session.get('usuario'):
        
        usuario_id = request.session.get('usuario')
        usuario = Usuario.objects.get(id=usuario_id)

        if request.method == 'POST':
            user_config = Configuracoes(usuario=usuario, niveis=request.POST.get('niveis'), categorias=request.POST.get('categorias_treino'))
            user_config.save()
            print(request.POST.get('categorias_treino'))
            print(request.POST.get('niveis'))
            return redirect('home')
        return render(request, 'configuracoes.html')
        
        
    
    else:
        return redirect('/auth/login/?status=2')

def gerar_treinoa(request):
    usuario_id = request.session.get('usuario')
    usuario = Usuario.objects.get(id=usuario_id)
    gerar_treino(usuario=usuario, parte_corpo='chest', alvo='biceps', letra_treino='A', grupo_muscular1='Peito', grupo_muscular2='Bíceps')
    return redirect('/home/fitness_app/?status=1')

def gerar_treinob(request):
    usuario_id = request.session.get('usuario')
    usuario = Usuario.objects.get(id=usuario_id)
    gerar_treino(usuario=usuario, parte_corpo='back', alvo='triceps', letra_treino='B', grupo_muscular1='Costas', grupo_muscular2='Triceps')
    return redirect('/home/fitness_app/?status=2')

def gerar_treinoc(request):
    usuario_id = request.session.get('usuario')
    usuario = Usuario.objects.get(id=usuario_id)
    gerar_treino(usuario=usuario, parte_corpo='lower legs', alvo='abs', letra_treino='C', grupo_muscular1='Perna', grupo_muscular2='Abdomen')
    return redirect('/home/fitness_app/?status=3')

def mainpage(request):
    return render(request, 'Portfolio/index.html')