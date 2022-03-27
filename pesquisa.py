from Models.sqlitedb import pesquisadb
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def votacao():
    retorno = True
    while retorno == True:
        try:
            voto = int(input('Seu voto ([1]sim/[2]não/[3]Não Opinar): '))
            data = datetime.now()
            vdata = str(datetime.timestamp(data)).strip('.')
            id = int(vdata[-5:])
            if voto == 1:
                print('votou sim, para ver resultado parcial, aperte 9')
                pesquisadb.computar_voto(id, True, False, False)
            elif voto == 2:
                print('votou não, para ver resultado parcial, aperte 9')
                pesquisadb.computar_voto(id, False, True, False)
            elif voto == 3:
                print('não opinou, para ver resultado parcial, aperte 9')
                pesquisadb.computar_voto(id, False, False, True)
            elif voto == 9:
                retorno = False
            else:
                print('não opinou, para ver resultado parcial, aperte 9')
                pesquisadb.computar_voto(id, False, False, True)
        except Exception as e:
            print(e)
            print('por favor, digitar apenas 1, 2, 3 ou 9')

def resultado_parcial():
    try:
        sem_opiniao = pesquisadb.contagem_sem_voto() #votos positivos
        voto_sim = pesquisadb.contagem_sim() #votos negativos
        voto_nao = pesquisadb.contagem_nao() #votos inválidos ou sem opiniao
        total_votos = pesquisadb.contagem_pessoas() #votos totais
        votos = ['Sim', 'Não', 'Não Opinou'] #nome coluna no x
        coluna = [voto_sim, voto_nao, sem_opiniao] # valores coluna x

        x = np.arange(len(votos))  # local onde variavel voto fica
        largura = 0.35  # largura coluna

        fig, ax = plt.subplots()
        resultado_grafico = ax.bar(x - largura/2, coluna, largura, label = 'Total de votos: {}'.format(total_votos))

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Votos')
        ax.set_title('Reunião de PI deve seguir as 20:00?')
        ax.set_xticks(x, votos)
        ax.legend()

        ax.bar_label(resultado_grafico, padding=3)

        fig.tight_layout()

        plt.show()
    except Exception as e:
        print(e)


def main():
    sqlitedb = pesquisadb
    sqlitedb.criar_banco_tabela()
    votacao()
    resultado_parcial()


if __name__ == "__main__":
    main()