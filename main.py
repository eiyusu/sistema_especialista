# UnB - Universidade de Brasília
# Introdução a Inteligência Artificial - Trabalho 02
# Victor Gabriel Rodrigues de Almeida - 140052399


#   Sintoma                     |   Dengue      |   Zika             |  Chikunguinya
#   Febre                       |   >38ºC       |   <38ºC            |  >38ºC
#   Duração da Febre            |   4 a 7 dias  |   1 ou 2 dias      |  2 ou 3 dias
#   Manchas na Pele             |   4º dia      |   1º ou 2º dia     |  2º ao 5º dia
#   Prob. Manchas               |   0,3 - 0,5   |   0,9 a 1          |  0,5
#   Frque. Dor Muscular         |   3/3         |   2/3              |  1/3
#   Frque. Dor Articular        |   1/3         |   2/3              |  3/3
#   Inten. Dor Articular        |   Leve        |   Leve/Moderada    |  Moderada/Intensa
#   Freque. Edema na Artic.    |   Raro        |   Frequente        |  Frequente
#   Inten. Endema na Artic.     |   X           |   Leve             |  Moderado/Intenso
#   Conjuntivite                |   Raro        |   0,5 - 0,9        |  0,3
#   Dor de cabeça               |   3/3         |   2/3              |  2/3
#   Coceira                     |   Leve        |   Moderada/Intensa |  Leve
#   Freq. Hipe. Gangl.          |   Leve        |   Intensa          |  Moderada
#   Freq. Disc. Hemo.           |   Moderada    |   Ausente          |  Leve
#   Acomet. Neuro.              |   Raro        |   Mais que outros  |  Raro (mais em neonatos)


class Doencas:
    def __init__(self, dengue, zyka, chikunguinya):
        self.dengue = dengue
        self.zyka = zyka
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
                         intensidade_muscular, dor_articulacao, intensidade_articulacao,
                         edema_articulacao, intensidade_edema, conjuntivite,
                         dor_cabeca, intensidade_cabeca, coceira, intensidade_coceira,
                         hipertrofia_ganglionar, intensidade_hipertrofia, discrasia_hemorragica,
                         intensidade_discrasia, acomentimento_neurologico):
    resultado = False

    if not febre and not manchas_pele and not dor_muscular and not dor_articulacao and not edema_articulacao and not conjuntivite and not dor_cabeca and not coceira and not hipertrofia_ganglionar and not discrasia_hemorragica and not acomentimento_neurologico:
        resultado = True
        print('\nProvavelmente, você não está com dengue, zika ou chikunguinya\n')

    if febre:
        trata_febre(grau_febre, tempo_febre)

    return resultado


def trata_febre(grau_febre, tempo_febre):

    return 0


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
                a = "Quantos graus celcius de febre você aprensentou?"
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
                print("Por quantos dias a febre persistiu? - Digite apenas o número de dias")
                while 1:
                    entrada = input()
                    if is_int(entrada):
                        if 0 < int(entrada) < 30:
                            tempo_febre = int(entrada)
                            break
                        else:
                            print("Números de dias incompatível com o esperado, escreva novamente (1 a 30 dias)")
                    else:
                        print("Tente novamente, apenas números inteiros são aceitos")

            # Manchas na pele
            manchas_pele = False
            dia_manchas = 0
            if apresentou('manchas na pele'):
                manchas_pele = True

                # Loop para saber o dia em que as manchas surgiram
                print("A partir de qual dia as manchas apareceram? Digite apenas um valor inteiro")
                while 1:
                    entrada = input()
                    if is_int(entrada):
                        if 0 < int(entrada) < 30:
                            dia_manchas = int(entrada)
                            break
                        else:
                            print("Dia de início do sintoma fora do esperado, escreva novamente (1º ao 30º dia)")
                    else:
                        print("Tente novamente, apenas números inteiros são aceitos")

            # Dor muscular
            dor_muscular = False
            intensidade_muscular = 0
            if apresentou('dor muscular'):
                dor_muscular = True
                intensidade_muscular = intensidade('da dor musuclar')

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
                                     intensidade_muscular, dor_articulacao, intensidade_articulacao,
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
