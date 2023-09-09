import emoji


def jogo_da_forca():
    import random

    print('Bem-Vindo(a) ao Marianna Game World!!')
    print('Deseja iniciar o jogo da forca?')
    resposta_da_entrada = input('(S/N): ').upper()
    print()

    if resposta_da_entrada != 'N':
        print('Insira o número correspondente a categoria da palavra desejada: ')
        print('-----------------------------------------------------------------------------------------------')
        print('1- FRUTAS')
        print('2- OBJETOS')
        print('3- CIDADES')
        print('4- ANIMAIS')
        print('5- PERSONAGENS')
        print('6- MARCAS')
        print('7- PARTE DO CORPO HUMANO')
        print('8- PROFISSÃO')
        print('9- CORES')
        print('10- FILMES')
        print('-----------------------------------------------------------------------------------------------')
        print()
        resposta_da_categoria = int(input('Número escolhido: '))

        frutas = {1: 'amora', 2: 'abacaxi', 3: 'melancia', 4: 'mamao', 5: 'morango', 6: 'framboesa', 7: 'carambola',
                  8: 'pitanga', 9: 'laranja', 10: 'abacate', 11: 'graviola', 14: 'cupuacu', 15: 'banana', 16: 'goiaba'}
        objetos = {1: 'apontador', 2: 'cadeira', 3: 'teclado', 4: 'computador', 5: 'tesoura', 6: 'caderno', 7: 'caneta',
                   8: 'liquidificador', 9: 'batedeira', 10: 'processador', 11: 'televisao', 12: 'armario', 13: 'gaveta',
                   14: 'chaveiro', 15: 'carregador', 16: 'microfone'}
        cidades = {1: 'bangkok', 2: 'toronto', 3: 'honolulu', 4: 'mumbai', 5: 'istambul', 6: 'londres', 7: 'moscou',
                   8: 'pequim', 9: 'sydney', 10: 'sorocaba', 11: 'campinas', 12: 'joinville', 13: 'fortaleza',
                   14: 'salvador', 15: 'curitiba', 16: 'uberlandia'}
        animais = {1: 'pinguim', 2: 'golfinho', 3: 'canguru', 4: 'tartaruga', 5: 'rinoceronte', 6: 'elefante',
                   7: 'lagarto', 8: 'tigre', 9: 'panda', 10: 'zebra', 11: 'tubarao', 12: 'macaco', 13: 'cobra',
                   14: 'coruja', 15: 'girafa', 16: 'galinha'}
        personagens = {1: 'batman', 2: 'harry potter', 3: 'james bond', 4: 'homer simpson', 5: 'tony stark',
                       6: 'sherlock holmes', 7: 'darth vader', 8: 'jack sparrow', 9: 'homem aranha',
                       10: 'homem de ferro', 11: 'indiana jones', 12: 'capitao america', 13: 'mulher maravilha',
                       14: 'rapunzel', 15: 'branca de neve', 16: 'ae3803'}
        marcas = {1: 'apple', 2: 'starbucks', 3: 'honda', 4: 'coca cola', 5: 'rolex', 6: 'facebook', 7: 'adidas',
                  8: 'pepsi', 9: 'toyota', 10: 'amazon', 11: 'riachuelo', 12: 'mercedes-benz', 13: 'disney',
                  14: 'samsung', 15: 'lenovo', 16: 'microsoft'}
        parte_do_corpo_humano = {1: 'nariz', 2: 'ae3803', 3: 'timpano', 4: 'estomago', 5: 'orelha', 6: 'canela',
                                 7: 'cilios', 8: 'queixo', 9: 'ombro', 10: 'femur', 11: 'cerebro', 12: 'braco',
                                 13: 'sobrancelha', 14: 'cabeca', 15: 'cabelo', 16: 'tornozelo'}
        profissao = {1: 'enfermeiro', 2: 'medico', 3: 'advogado', 4: 'bombeiro', 5: 'programador', 6: 'engenheiro',
                     7: 'professor', 8: 'ator', 9: 'fisioterapeuta', 10: 'psicologo', 11: 'juiz', 12: 'atleta',
                     13: 'secretario', 14: 'estilista', 15: 'designer', 16: 'coreografo'}
        cores = {1: 'azul marinho', 2: 'verde claro', 3: 'vermelho', 4: 'anil', 5: 'violeta', 6: 'amarelo', 7: 'marrom',
                 8: 'cinza escuro', 9: 'rosa claro', 10: 'branco', 11: 'laranja', 12: 'preto', 13: 'roxo', 14: 'coral',
                 15: 'ciano', 16: 'azul claro'}
        filmes = {1: 'avatar', 2: 'parasita', 3: 'matrix', 4: 'titanic', 5: 'interestelar', 6: 'tubarao',
                  7: 'pulp fiction', 8: 'clube da luta', 9: 'exterminador do futuro', 10: 'sexto sentido',
                  11: 'senhor dos aneis', 12: 'vingadores', 13: 'harry potter', 14: 'divergente', 15: 'jogos vorazes',
                  16: 'jogos mortais'}

        numero_sorteado = random.randint(1, 16)

        if resposta_da_categoria == 1:
            palavra_sorteada = frutas[numero_sorteado]
        elif resposta_da_categoria == 2:
            palavra_sorteada = objetos[numero_sorteado]
        elif resposta_da_categoria == 3:
            palavra_sorteada = cidades[numero_sorteado]
        elif resposta_da_categoria == 4:
            palavra_sorteada = animais[numero_sorteado]
        elif resposta_da_categoria == 5:
            palavra_sorteada = personagens[numero_sorteado]
        elif resposta_da_categoria == 6:
            palavra_sorteada = marcas[numero_sorteado]
        elif resposta_da_categoria == 7:
            palavra_sorteada = parte_do_corpo_humano[numero_sorteado]
        elif resposta_da_categoria == 8:
            palavra_sorteada = profissao[numero_sorteado]
        elif resposta_da_categoria == 9:
            palavra_sorteada = cores[numero_sorteado]
        elif resposta_da_categoria == 10:
            palavra_sorteada = filmes[numero_sorteado]

        print()
        print('-----------------------------------------------------------------------------------------------')
        print('CONSIDERAÇÕES INICIAIS:')
        print('1- As palavras não possuem (Ç), acentos ou caracteres especiais.')
        print('2- Os espaços que aparecerem sem traço configuram espaço entre as palavras.')
        print('3- Seu número de tentativas erradas é calculado pelo número de letras diferentes da palavra + 7.')
        print('------------------------------------------------------------------------------------------------')
        print()
        print('Iniciando o jogo! VALENDO!')
        print(f"A sua palavra tem {len(palavra_sorteada)} letras.")
        tentativas = 'Letras tentadas: '
        lista_de_tentativas = []
        print()
        print('  ____________')
        print(' |            |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('_|_')
        print()

        palavra = []
        for g in range(len(palavra_sorteada)):
            if palavra_sorteada[g] == ' ':
                palavra.append(' ')
            else:
                palavra.append('_')

        print(tentativas)
        print('PALAVRA:', palavra)
        letra = input('Insira uma letra: ').lower()
        print()
        if letra[0] in palavra_sorteada:
            for j in range(len(palavra_sorteada)):
                if palavra_sorteada[j] == letra[0]:
                    palavra.pop(j)
                    palavra.insert(j, letra[0])
        else:
            tentativas += letra[0].upper() + ' / '
            lista_de_tentativas.append(letra[0])

        print(tentativas)
        print('PALAVRA:', palavra)

        venceu = 0
        while len(lista_de_tentativas) < len(set(palavra_sorteada)) + 7 and venceu == 0:
            letra = input('Insira uma letra: ').lower()
            print()
            if letra[0] in palavra_sorteada:
                for j in range(len(palavra_sorteada)):
                    if palavra_sorteada[j] == letra[0]:
                        palavra.pop(j)
                        palavra.insert(j, letra[0])
            else:
                if letra[0] not in lista_de_tentativas:
                    tentativas += letra[0].upper() + ' / '
                    lista_de_tentativas.append(letra[0])

            print(tentativas)
            print('PALAVRA:', palavra)

            if '_' not in palavra and len(lista_de_tentativas) <= len(set(palavra_sorteada)) + 7:
                print()
                print(' _________________________________________')
                print('|                                         |')
                print('| UHUULLL!! PARABEEENNNNSSS VOCE GANHOU!! |')
                print('|_________________________________________|')
                print()
                venceu = 1

        if venceu == 0:
            print()
            print(' ________________________________________________________')
            print('|                                                        |')
            print('| AH QUE PENA!!!! :( minha IA é muito inteligente mesmo. |')
            print('|________________________________________________________|')
            print()


def jokenpo():
    import random

    print('Bem-Vindo(a) ao Marianna Game World!!')
    print('Deseja iniciar o jogo do jokenpo?')
    resposta_da_entrada = input('(S/N): ').upper()

    if resposta_da_entrada != 'N':
        possibilidades = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
        pontos_da_maquina = 0
        pontos_da_pessoa = 0

        print()
        print('-----------------------------------------------------------------------------------------------')
        print('CONSIDERAÇÕES INICIAIS:')
        print('1- Serão realizadas rodadas até que um dos dois placares computem 3 pontos.')
        print('2- O placar é dado por: rodadas ganhas da máquina x rodadas que você ganhou.')
        print('------------------------------------------------------------------------------------------------')
        print()

        print(' ____________________________')
        print('|                            |')
        print('| INICIANDO O JOGO, VALENDO! |')
        print('|____________________________|')
        print()
        while pontos_da_maquina < 3 and pontos_da_pessoa < 3:
            print(' _________________________________________________________')
            print('|                                                         |')
            print(f'|  PLACAR DO JOGO: {pontos_da_maquina} X {pontos_da_pessoa}                                  |')
            print('|________________________________________________________ |')
            escolha_da_maquina = possibilidades[random.randint(1, 3)]
            escolha_da_pessoa = input(' Digite se deseja pedra, papel ou tesoura: ').lower()
            print()

            if escolha_da_maquina == 'pedra' and escolha_da_pessoa == 'papel':
                pontos_da_pessoa += 1
                print(' Você escolheu papel.')
                print(' IA escolheu pedra.')
                print(' Você ganhou a rodada!!')
                print()
            elif escolha_da_maquina == 'papel' and escolha_da_pessoa == 'pedra':
                pontos_da_maquina += 1
                print(' Você escolheu pedra.')
                print(' IA escolheu papel.')
                print(' IA ganhou a rodada hihihih')
                print()
            elif escolha_da_maquina == 'tesoura' and escolha_da_pessoa == 'papel':
                pontos_da_maquina += 1
                print(' Você escolheu papel.')
                print(' IA escolheu tesoura.')
                print(' IA ganhou a rodada hihihih')
                print()
            elif escolha_da_maquina == 'papel' and escolha_da_pessoa == 'tesoura':
                pontos_da_pessoa += 1
                print(' Você escolheu tesoura.')
                print(' IA escolheu papel.')
                print(' Você ganhou a rodada!!')
                print()
            elif escolha_da_maquina == 'pedra' and escolha_da_pessoa == 'tesoura':
                pontos_da_maquina += 1
                print(' Você escolheu tesoura.')
                print(' IA escolheu pedra.')
                print(' IA ganhou a rodada hihihih')
                print()
            elif escolha_da_maquina == 'tesoura' and escolha_da_pessoa == 'pedra':
                pontos_da_pessoa += 1
                print(' Você escolheu pedra.')
                print(' IA escolheu tesoura.')
                print(' Você ganhou a rodada!!')
                print()

            elif escolha_da_maquina == escolha_da_pessoa:
                print(' EMPATEEEE QUE DROGA!!!')
                print()

        if pontos_da_maquina == 3:
            print()
            print(' ________________________________________________________')
            print('|                                                        |')
            print('| AH QUE PENA!!!! :( minha IA é muito inteligente mesmo. |')
            print('|________________________________________________________|')
            print()

        else:
            print()
            print(' _________________________________________')
            print('|                                         |')
            print('| UHUULLL!! PARABEEENNNNSSS VOCE GANHOU!! |')
            print('|_________________________________________|')
            print()


def adivinhacao():
    import random

    print('Bem-Vindo(a) ao Marianna Game World!!')
    print('Deseja iniciar o jogo da adivinhação?')
    resposta_da_entrada = input('(S/N): ').upper()

    if resposta_da_entrada != 'N':
        numero_da_IA = random.randint(1, 100)

        print()
        print('-----------------------------------------------------------------------------------------------')
        print('CONSIDERAÇÕES INICIAIS:')
        print('1- Serão realizadas 14 rodadas, logo você tem 14 chances de acertar.')
        print('2- Número mais 10 unidades acima ou abaixo: LONGE.')
        print('3- Número menos ou igual de 10 unidades acima ou abaixo: PERTO.')
        print('------------------------------------------------------------------------------------------------')
        print()

        print(' ____________________________')
        print('|                            |')
        print('| INICIANDO O JOGO, VALENDO! |')
        print('|____________________________|')
        print()
        numero_que_chutou = int(input('Digite um número entre 1 e 100, (1 e 100) são inclusos: '))
        lista = [numero_da_IA, numero_que_chutou]
        diferenca_entre_os_valores = max(lista) - min(lista)
        if diferenca_entre_os_valores == 0:
            print('PO PARABÉNS MALUCAO!!')
        elif diferenca_entre_os_valores > 10:
            print('--->  LONGE')
            print()
        elif diferenca_entre_os_valores <= 10:
            print('--->  PERTO')
            print()
        i = 1
        v = 0
        while i < 14 and v == 0:
            numero_que_chutou = int(input('Digite um número entre 1 e 100, (1 e 100) são inclusos: '))
            lista = [numero_da_IA, numero_que_chutou]
            diferenca_entre_os_valores = max(lista) - min(lista)
            if diferenca_entre_os_valores == 0:
                print()
                print('PO PARABÉNS MALUCAO!!')
                v = 1
            elif diferenca_entre_os_valores > 10:
                print('--->  LONGE')
                print()
            elif diferenca_entre_os_valores <= 10:
                print('--->  PERTO')
                print()
            i += 1

        if i == 14:
            print('UMA PENA MESMO NÉ, PARECE QUE VOCÊ PRECISA CONSULTAR SUA SORTE')
            print(f'O número escolhido era {numero_da_IA}.')
        else:
            print('VOCE DEVIA VIRAR CARTOMANTE')
        print()


print('Será que você tem o que é preciso para vencer a minha IA?: ')
resposta = input('(S/N): ').upper()
print()
if resposta != 'N':
    while resposta != 'N':
        print('Você quer jogar qual joguinho? Digite o número correspondente ao jogo.')
        print()
        print('1- jogo da forca')
        print('2- jokenpo')
        print('3- adivinhação')
        print()
        resposta_da_pessoa = int(input('Digite o número: '))
        print()
        if resposta_da_pessoa == 1:
            jogo_da_forca()
        elif resposta_da_pessoa == 2:
            jokenpo()
        elif resposta_da_pessoa == 3:
            adivinhacao()
        print('Você ainda quer jogar fracote?', emoji.emojize(':thumbs_up:'))
        resposta = input('(S/N): ').upper()
        print()

print('Okay nos vemos depois....')
print()

# Colocar na forca que letras com mais de 1 caracteres nao sao validas
