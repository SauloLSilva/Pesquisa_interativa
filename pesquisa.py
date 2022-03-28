from Models.sqlitedb import pesquisadb
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Process

def votacao():
    while True:
        try:
            voto = int(input('Seu voto ([1]sim/[2]não/[3]Não Opinar): '))
            data = datetime.now()
            vdata = str(datetime.timestamp(data)).strip('.')
            id = int(vdata[-5:])
            if voto == 1:
                print('votou sim')
                pesquisadb.computar_voto(id, True, False, False)
            elif voto == 2:
                print('votou não')
                pesquisadb.computar_voto(id, False, True, False)
            elif voto == 3:
                print('não opinou')
                pesquisadb.computar_voto(id, False, False, True)
            else:
                print('não opinou')
                pesquisadb.computar_voto(id, False, False, True)
        except Exception as e:
            print(e)
            print('por favor, digitar apenas 1, 2 ou 3')

def resultado_parcial():
    while True:
        try:
            total_votos = pesquisadb.contagem_pessoas() #votos totais
            if total_votos != 0:
                sem_opiniao = pesquisadb.contagem_sem_voto() #votos inválidos ou sem opiniao
                voto_sim = pesquisadb.contagem_sim() #votos positivos
                voto_nao = pesquisadb.contagem_nao() #votos negativos
                porc_voto_sim = round(((100* voto_sim)/ total_votos),2)
                porc_voto_nao = round(((100* voto_nao)/ total_votos),2)
                porc_sem_opiniao = round(((100* sem_opiniao)/ total_votos),2)
                votos = ['Sim', 'Não', 'Não Opinou'] #nome coluna no x
                coluna = [porc_voto_sim, porc_voto_nao, porc_sem_opiniao] # valores coluna x

                x = np.arange(len(votos))  # local onde variavel voto fica
                largura = 0.35  # largura coluna

                plt.ion()
                fig, ax = plt.subplots()
                resultado_grafico = ax.bar(x - largura/50, coluna, largura, label = 'Total de votos: {}'.format(total_votos))

                ax.set_ylabel('Votos (em %)') #label de y
                ax.set_title('Reunião de PI deve seguir as 20:00?') #título
                ax.set_xticks(x, votos) # label de x
                ax.legend()

                ax.bar_label(resultado_grafico, padding=3)

                fig.tight_layout()

                plt.draw()
                plt.pause(30)
                plt.close()
            else:
                pass

        except Exception as e:
            print(e)


def main():
    sqlitedb = pesquisadb
    sqlitedb.criar_banco_tabela()
    t_vot = Process(target=resultado_parcial)
    t_vot.start()
    votacao()



if __name__ == "__main__":
    main()