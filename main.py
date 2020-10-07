# UnB - Universidade de Brasília
# Introdução a Inteligência Artificial - Trabalho 02
# Victor Gabriel Rodrigues de Almeida - 140052399


#   Sintoma                     |   Dengue      |   Zika             |  Chikunguinya
#   Febre                       |   >38ºC       |   <38ºC            |  >38ºC
#   Duração da Febre            |   4 a 7 dias  |   1 ou 2 dias      |  2 ou 3 dias
#   Manchas na Pele             |   4º dia      |   1º ou 2º dia     |  2º ao 5º dia
#   Prob. Manchas               |   0,3 - 0,5   |   0,9 a 1          |  0,5
#   Freq. Dor Muscular          |   3/3         |   2/3              |  1/3
#   Freq. Dor Articular         |   1/3         |   2/3              |  3/3
#   Inten. Dor Articular        |   Leve        |   Leve/Moderada    |  Moderada/Intensa
#   Freq. Edema na Artic.       |   Raro        |   Frequente        |  Frequente
#   Inten. Endema na Artic.     |   X           |   Leve             |  Moderado/Intenso
#   Conjuntivite                |   Raro        |   0,5 - 0,9        |  0,3
#   Dor de cabeça               |   3/3         |   2/3              |  2/3
#   Coceira                     |   Leve        |   Moderada/Intensa |  Leve
#   Freq. Hipe. Gangl.          |   Leve        |   Intensa          |  Moderada
#   Freq. Disc. Hemo.           |   Moderada    |   Ausente          |  Leve
#   Acomet. Neuro.              |   Raro        |   Mais que outros  |  Raro (mais em neonatos)


p_dengue = 1/3
p_zika = 1/3
p_chikungunya = 1/3


class Doencas:
    def __init__(self, dengue, zika, chikunguinya):
        self.dengue = dengue
        self.zika = zika
        self.chikunguinya = chikunguinya


# Função auxiliar que verifica se uma string pode ser traduzida diretamente para número inteiro
def is_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


# Função auxiliar para perguntar se a pessoa apresentou cada um dos sintomas
def apresentou(sintoma):
    print("Você aprensentou " + sintoma + "?")
    print("[1] Sim     |     [2] Não")
    while 1:
        entrada = input()
        if entrada == '1':
            return True
        elif entrada == '2':
            return False
        else:
            print("Entre um valor válido: [1] ou [2]")


# Função genérica para saber intensidade de um sintoma
def intensidade(sintoma):
    print("Qual a intensidade " + sintoma + "? Digite o número correspondente a opção")
    print("[1] Leve     |     [2] Moderado     |     [3] Intenso")
    while 1:
        intensidade_sintoma = input()
        if is_int(intensidade_sintoma):
            if 0 < int(intensidade_sintoma) < 4:
                return int(intensidade_sintoma)
            else:
                print("Digite um valor dentro das opções disponíveis")
        else:
            print("Tente novamente, apenas números inteiros são aceitos")


# Função do sistema especialista que entregará um resultado a partir das informações coletadas
def sistema_especialista(febre, grau_febre, tempo_febre, manchas_pele, dia_manchas, dor_muscular,
                         dor_articulacao, intensidade_articulacao,
                         edema_articulacao, intensidade_edema, conjuntivite,
                         dor_cabeca, intensidade_cabeca, coceira, intensidade_coceira,
                         hipertrofia_ganglionar, intensidade_hipertrofia, discrasia_hemorragica,
                         intensidade_discrasia, acomentimento_neurologico):

    eventos_dengue = []
    eventos_zika = []
    eventos_chikungunya = []
    doente = True

    if not febre and not manchas_pele and not dor_muscular and not dor_articulacao and not edema_articulacao and not conjuntivite and not dor_cabeca and not coceira and not hipertrofia_ganglionar and not discrasia_hemorragica and not acomentimento_neurologico:
        doente = False
        print('\nProvavelmente, você não está com dengue, zika ou chikunguinya\n')

    if not febre and doente:
        febre_chance = febre_prob()
        eventos_dengue.append(febre_chance.dengue)
        eventos_zika.append(febre_chance.zika)
        eventos_chikungunya.append(febre_chance.chikunguinya)

    if febre:
        temperatura = febre_temperatura(grau_febre)
        duracao_febre = febre_duracao(tempo_febre)
        eventos_dengue.append(temperatura.dengue)
        eventos_zika.append(temperatura.zika)
        eventos_chikungunya.append(temperatura.chikunguinya)
        eventos_dengue.append(duracao_febre.dengue)
        eventos_zika.append(duracao_febre.zika)
        eventos_chikungunya.append(duracao_febre.chikunguinya)

    if manchas_pele:
        mancha_chance = mancha_prob(dia_manchas)
        eventos_dengue.append(mancha_chance.dengue)
        eventos_zika.append(mancha_chance.zika)
        eventos_chikungunya.append(mancha_chance.chikunguinya)

    if dor_muscular:
        muscular_chance = muscular_prob()
        eventos_dengue.append(muscular_chance.dengue)
        eventos_zika.append(muscular_chance.zika)
        eventos_chikungunya.append(muscular_chance.chikunguinya)

    if dor_articulacao:
        articulacao_chance = articular_prob()
        articulacao_intensidade = articular_dor(intensidade_articulacao)
        eventos_dengue.append(articulacao_chance.dengue)
        eventos_zika.append(articulacao_chance.zika)
        eventos_chikungunya.append(articulacao_chance.chikunguinya)
        eventos_dengue.append(articulacao_intensidade.dengue)
        eventos_zika.append(articulacao_intensidade.zika)
        eventos_chikungunya.append(articulacao_intensidade.chikunguinya)

    if edema_articulacao:
        edema_chance = edema_prob()
        edema_intensidade = edema_dor(intensidade_edema)
        eventos_dengue.append(edema_chance.dengue)
        eventos_zika.append(edema_chance.zika)
        eventos_chikungunya.append(edema_chance.chikunguinya)
        eventos_dengue.append(edema_intensidade.dengue)
        eventos_zika.append(edema_intensidade.zika)
        eventos_chikungunya.append(edema_intensidade.chikunguinya)

    if conjuntivite:
        conjuntivite_chance = conjuntivite_prob()
        eventos_dengue.append(conjuntivite_chance.dengue)
        eventos_zika.append(conjuntivite_chance.zika)
        eventos_chikungunya.append(conjuntivite_chance.chikunguinya)

    if dor_cabeca:
        cabeca_chance = cabeca_prob()
        cabeca_intensidade = cabeca_dor(intensidade_cabeca)
        eventos_dengue.append(cabeca_chance.dengue)
        eventos_zika.append(cabeca_chance.zika)
        eventos_chikungunya.append(cabeca_chance.chikunguinya)
        eventos_dengue.append(cabeca_intensidade.dengue)
        eventos_zika.append(cabeca_intensidade.zika)
        eventos_chikungunya.append(cabeca_intensidade.chikunguinya)

    if coceira:
        coceira_intensidade = coceira_dor(intensidade_coceira)
        eventos_dengue.append(coceira_intensidade.dengue)
        eventos_zika.append(coceira_intensidade.zika)
        eventos_chikungunya.append(coceira_intensidade.chikunguinya)

    if hipertrofia_ganglionar:
        hipertrofia_intensidade = hipertrofia_dor(intensidade_hipertrofia)
        eventos_dengue.append(hipertrofia_intensidade.dengue)
        eventos_zika.append(hipertrofia_intensidade.zika)
        eventos_chikungunya.append(hipertrofia_intensidade.chikunguinya)

    if discrasia_hemorragica:
        discrasia_chance = discrasia_prob()
        discrasia_intensidade = discrasia_dor(intensidade_discrasia)
        eventos_dengue.append(discrasia_chance.dengue)
        eventos_zika.append(discrasia_chance.zika)
        eventos_chikungunya.append(discrasia_chance.chikunguinya)
        eventos_dengue.append(discrasia_intensidade.dengue)
        eventos_zika.append(discrasia_intensidade.zika)
        eventos_chikungunya.append(discrasia_intensidade.chikunguinya)

    if acomentimento_neurologico:
        acometimento_chance = acometimento_prob()
        eventos_dengue.append(acometimento_chance.dengue)
        eventos_zika.append(acometimento_chance.zika)
        eventos_chikungunya.append(acometimento_chance.chikunguinya)

    if len(eventos_dengue) > 0 and len(eventos_zika) > 0 and len(eventos_chikungunya) > 0:
        probabilidades = bayesiano(eventos_dengue, eventos_zika, eventos_chikungunya)

        if probabilidades.dengue > probabilidades.zika and probabilidades.dengue > probabilidades.chikunguinya:
            print('\n***************************************************************')
            print('Doença com maior probabilidade: DENGUE')
            print('***************************************************************\n')

        if probabilidades.zika > probabilidades.dengue and probabilidades.zika > probabilidades.chikunguinya:
            print('\n***************************************************************')
            print('Doença com maior probabilidade: ZIKA')
            print('***************************************************************\n')

        if probabilidades.chikunguinya > probabilidades.zika and probabilidades.chikunguinya > probabilidades.dengue:
            print('\n***************************************************************')
            print('Doença com maior probabilidade: CHIKUNGUNYA')
            print('***************************************************************\n')


# Função de cálculo das probs Bayesianas
def bayesiano(eventos_dengue, eventos_zika, eventos_chikungunya):
    numerador_dengue = p_dengue
    numerador_zika = p_zika
    numerador_chikungunya = p_chikungunya

    for i in range(0, len(eventos_dengue)):
        numerador_dengue = numerador_dengue * eventos_dengue[i]
        numerador_zika = numerador_zika * eventos_zika[i]
        numerador_chikungunya = numerador_chikungunya * eventos_chikungunya[i]

    denominador = numerador_dengue + numerador_zika + numerador_chikungunya
    dengue = numerador_dengue/denominador
    zika = numerador_zika/denominador
    chikungunya = numerador_chikungunya/denominador

    return Doencas(dengue, zika, chikungunya)


# Função que retorna a probabilidade de cada doença dada a presença ou não de febre
def febre_prob():
    dengue = 0.05
    zika = 0.5
    chikungunya = 0.05
    return Doencas(dengue, zika, chikungunya)


# Função que retorna a probabilidade de cada doença dada a temperatura da febre
def febre_temperatura(grau_febre):
    if grau_febre < 39:
        dengue = 0.1
        chikungunya = 0.1
        zika = 1
    else:
        dengue = 0.6
        zika = 0.1
        chikungunya = (grau_febre/3)-(38/3)
    return Doencas(dengue, zika, chikungunya)


# Função que retorna as probabilidades de cada doença dada a duração da febre
def febre_duracao(tempo_febre):
    if 0 < tempo_febre <= 2:
        dengue = tempo_febre / 7
        zika = tempo_febre / 2
        chikungunya = tempo_febre / 3
    elif 2 < tempo_febre <= 3:
        dengue = tempo_febre / 7
        zika = 0.1
        chikungunya = tempo_febre / 3
    else:
        dengue = tempo_febre / 7
        zika = 0.1
        chikungunya = 0.3
    return Doencas(dengue, zika, chikungunya)


# Função que retorna a probabilidade de cada doença dado o dia de surgimento das manchas
def mancha_prob(dia_manchas):
    if dia_manchas <= 2:
        dengue = 0.3
        zika = 1
        chikungunya = 0.5
    elif 2 < dia_manchas <= 4:
        dengue = 0.3
        zika = 0.9
        chikungunya = 0.5
    else:
        dengue = 0.5
        zika = 0.9
        chikungunya = 0.5
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dado o surgimento de dor muscular
def muscular_prob():
    dengue = 1
    zika = 2 / 3
    chikungunya = 1 / 3
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dado o surgimento de dor articular
def articular_prob():
    dengue = 1 / 3
    zika = 2 / 3
    chikungunya = 1
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dada a intensidade da dor articular
def articular_dor(intensidade_articulacao):
    if intensidade_articulacao == 1:
        dengue = 0.9
        zika = 0.5
        chikungunya = 0.1
    elif intensidade_articulacao == 2:
        dengue = 0.1
        zika = 0.5
        chikungunya = 0.5
    else:
        dengue = 0.1
        zika = 0.1
        chikungunya = 0.9
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dado o surgimento de edema
def edema_prob():
    dengue = 0.05
    zika = 0.5
    chikungunya = 0.5
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dada a intensidade do edema
def edema_dor(intensidade_edema):
    if intensidade_edema == 1:
        dengue = 0.01
        zika = 0.8
        chikungunya = 0.2
    elif intensidade_edema == 2:
        dengue = 0.01
        zika = 0.2
        chikungunya = 0.8
    else:
        dengue = 0.01
        zika = 0.2
        chikungunya = 0.8
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dado o surgimento de conjuntivite
def conjuntivite_prob():
    dengue = 0.05
    zika = 0.7
    chikungunya = 0.3
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dado o surgimento de dor de cabeça
def cabeca_prob():
    dengue = 1
    zika = 2 / 3
    chikungunya = 2 / 3
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dada a intensidade da dor de cabeça
def cabeca_dor(intensidade_cabeca):
    if intensidade_cabeca == 1:
        dengue = 1 / 3
        zika = 1 / 3
        chikungunya = 1 / 3
    elif intensidade_cabeca == 2:
        dengue = 0.1
        zika = 2 / 3
        chikungunya = 2 / 3
    else:
        dengue = 1
        zika = 0.1
        chikungunya = 0.1
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dada a intensidade da coceira
def coceira_dor(intensidade_coceira):
    if intensidade_coceira == 1:
        dengue = 0.9
        zika = 0.1
        chikungunya = 0.9
    elif intensidade_coceira == 2:
        dengue = 0.1
        zika = 0.9
        chikungunya = 0.1
    else:
        dengue = 0.1
        zika = 0.9
        chikungunya = 0.1
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dada a intensidade da hipertrofia
def hipertrofia_dor(intensidade_hipertrofia):
    if intensidade_hipertrofia == 1:
        dengue = 0.9
        zika = 0.1
        chikungunya = 0.1
    elif intensidade_hipertrofia == 2:
        dengue = 0.1
        zika = 0.1
        chikungunya = 0.9
    else:
        dengue = 0.1
        zika = 0.9
        chikungunya = 0.1
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dado o surgimento de discrasia
def discrasia_prob():
    dengue = 0.5
    zika = 0
    chikungunya = 0.5
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dada a intensidade da discrasia
def discrasia_dor(intensidade_discrasia):
    if intensidade_discrasia == 1:
        dengue = 0.1
        zika = 0
        chikungunya = 0.9
    elif intensidade_discrasia == 2:
        dengue = 0.9
        zika = 0
        chikungunya = 0.1
    else:
        dengue = 0.5
        zika = 0
        chikungunya = 0.5
    return Doencas(dengue, zika, chikungunya)


# Função que retorna probabilidade de cada doença dado o surgimento de acometimento neurológico
def acometimento_prob():
    dengue = 0.05
    zika = 0.15
    chikungunya = 0.05
    return Doencas(dengue, zika, chikungunya)


def main():
    print("\nSistema de Diagnósticos de Doenças - Dengue | Zika | Chikunguinya\n")

    # Loop principal com requisição das informações necessárias
    print('[1] Diagnosticar\n[2] Sair')
    entrada = input()
    while 1:
        if entrada == '2':
            break
        elif entrada == '1':

            # Febre
            febre = False
            grau_febre = 0
            tempo_febre = 0
            if apresentou('febre'):
                febre = True
                # Loop para ver a temperatura
                a = "Quantos graus celcius de febre você aprensentou? Digite valor inteiro [36 a 41]"
                b = " Escreva apenas números da maior temperatura medida"
                print(a + b)
                while 1:
                    entrada = input()
                    if is_int(entrada):
                        if 35 < int(entrada) < 42:
                            grau_febre = int(entrada)
                            break
                        else:
                            print("Temperatura fora dos parâmetros aceitáveis, escreva novamente")
                    else:
                        print("Tente novamente, apenas números inteiros são aceitos")

                # Loop para ver a duração da febre
                print("Por quantos dias a febre persistiu? - Digite apenas o número de dias [1 a 7]")
                while 1:
                    entrada = input()
                    if is_int(entrada):
                        if 0 < int(entrada) < 8:
                            tempo_febre = int(entrada)
                            break
                        else:
                            print("Números de dias incompatível com o esperado, escreva novamente (1 a 7 dias)")
                    else:
                        print("Tente novamente, apenas números inteiros são aceitos")

            # Manchas na pele
            manchas_pele = False
            dia_manchas = 0
            if apresentou('manchas na pele'):
                manchas_pele = True

                # Loop para saber o dia em que as manchas surgiram
                print("A partir de qual dia as manchas apareceram? Digite apenas um valor inteiro [1 a 5]")
                while 1:
                    entrada = input()
                    if is_int(entrada):
                        if 0 < int(entrada) < 6:
                            dia_manchas = int(entrada)
                            break
                        else:
                            print("Dia de início do sintoma fora do esperado, escreva novamente (1º ao 5º dia)")
                    else:
                        print("Tente novamente, apenas números inteiros são aceitos")

            # Dor muscular
            dor_muscular = False
            if apresentou('dor muscular'):
                dor_muscular = True

            # Dor nas articulações
            dor_articulacao = False
            intensidade_articulacao = 0
            if apresentou('dor nas articulações'):
                dor_articulacao = True
                intensidade_articulacao = intensidade('da dor nas articulações')

            # Edema na articulação
            edema_articulacao = False
            intensidade_edema = 0
            if apresentou('edema na articulação'):
                edema_articulacao = True
                intensidade_edema = intensidade('do edema nas articulações')

            # Conjuntivite
            conjuntivite = False
            if apresentou('conjuntivite'):
                conjuntivite = True

            # Dor de cabeça
            dor_cabeca = False
            intensidade_cabeca = 0
            if apresentou('dor de cabeça'):
                dor_cabeca = True
                intensidade_cabeca = intensidade('da dor de cabeça')

            # Coceira
            coceira = False
            intensidade_coceira = 0
            if apresentou('coceira'):
                coceira = True
                intensidade_coceira = intensidade('da coceira')

            # Hipertrofia ganglionar
            hipertrofia_ganglionar = False
            intensidade_hipertrofia = 0
            if apresentou('hipertrofia ganglionar'):
                hipertrofia_ganglionar = True
                intensidade_hipertrofia = intensidade('da hipertrofia ganglionar')

            # Discrasia hemorrágica
            discrasia_hemorragica = False
            intensidade_discrasia = 0
            if apresentou('discrasia hemorrágica'):
                discrasia_hemorragica = True
                intensidade_discrasia = intensidade('da discrasia hemorrágica')

            # Acometimento neurológico
            acomentimento_neurologico = False
            if apresentou('acometimento neurológico'):
                acomentimento_neurologico = True

            # Resultado
            sistema_especialista(febre, grau_febre, tempo_febre, manchas_pele, dia_manchas, dor_muscular,
                                 dor_articulacao, intensidade_articulacao,
                                 edema_articulacao, intensidade_edema, conjuntivite,
                                 dor_cabeca, intensidade_cabeca, coceira, intensidade_coceira,
                                 hipertrofia_ganglionar, intensidade_hipertrofia, discrasia_hemorragica,
                                 intensidade_discrasia, acomentimento_neurologico)

            print('Deseja realizar novo dignóstico?\n[1] Sim     |     [2] Não')
            while 1:
                entrada = input()
                if entrada == '1' or entrada == '2':
                    break
                else:
                    print("Entre um valor válido: [1] ou [2]")
            if entrada == '2':
                break
            else:
                print('\n\nResponda novamente o questionário\n')

        # Não faz diagnóstico e nem sai do programa
        else:
            print("Comando não reconhecido")

    print("\nPrograma encerrado")


if __name__ == '__main__':
    main()
